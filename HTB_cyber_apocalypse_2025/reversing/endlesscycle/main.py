#!/usr/bin/env python3

from pwn import xor

"""
Code généré dynamiquement par l'exécutable

; === Affichage "What is the flag?" ===
0x7ffff7fbf000:    push    rbp
0x7ffff7fbf001:    mov     rbp, rsp
0x7ffff7fbf004:    push    0x101213e
0x7ffff7fbf009:    xor     dword ptr [rsp], 0x1010101
0x7ffff7fbf010:    movabs  rax, 0x67616c6620656874        ; "the flag"
0x7ffff7fbf015:    push    rax
0x7ffff7fbf016:    movabs  rax, 0x2073692074616857        ; "What is "
0x7ffff7fbf01b:    push    rax
0x7ffff7fbf01c:    push    0x1
0x7ffff7fbf01e:    pop     rax                            ; rax = syscall 1 (write)
0x7ffff7fbf01f:    push    0x1
0x7ffff7fbf021:    pop     rdi                            ; stdout
0x7ffff7fbf022:    push    0x12
0x7ffff7fbf024:    pop     rdx                            ; len = 0x12
0x7ffff7fbf025:    mov     rsi, rsp                       ; rsi = "What is the flag?"
0x7ffff7fbf027:    syscall                                ; write(1, rsi, rdx)

; === Lecture de l'entrée utilisateur ===
0x7ffff7fbf029:    sub     rsp, 0x100
0x7ffff7fbf030:    mov     r12, rsp
0x7ffff7fbf033:    xor     eax, eax                       ; syscall 0 (read)
0x7ffff7fbf035:    xor     edi, edi                       ; stdin
0x7ffff7fbf037:    xor     edx, edx
0x7ffff7fbf039:    mov     dh, 0x1                        ; edx = 0x100
0x7ffff7fbf03b:    mov     rsi, r12                       ; buffer = r12
0x7ffff7fbf03e:    syscall                                ; read(0, r12, 0x100)

; === Prétraitement et test des 4 premiers octets ===
0x7ffff7fbf040:    test    rax, rax
0x7ffff7fbf043:    je      0x7ffff7fbf082                 ; si lecture échouée, fin
0x7ffff7fbf045:    push    0x1a
0x7ffff7fbf047:    pop     rax
0x7ffff7fbf048:    mov     rcx, r12
0x7ffff7fbf04b:    xor     rax, rax
0x7ffff7fbf04d:    xor     dword ptr [rcx], 0xbeefcafe
0x7ffff7fbf053:    cmp     rax, qword ptr [rcx]          ; (en réalité, compare les 4 bytes modifiés à 0)
0x7ffff7fbf056:    je      0x7ffff7fbf082

; === Comparaison du reste du flag ===
0x7ffff7fbf058:    mov     rcx, 0x1a                      ; nombre d'octets à comparer
0x7ffff7fbf05f:    mov     rdi, r12
0x7ffff7fbf062:    lea     rsi, [rip + 0x12]              ; rsi pointe sur chaîne cible
0x7ffff7fbf066:    mov     rdx, rcx
0x7ffff7fbf069:    repz cmpsb byte ptr es:[rdi], byte ptr ds:[rsi]
0x7ffff7fbf06b:    sete    al
0x7ffff7fbf06e:    movzx   eax, al

; === Fin du shellcode ===
0x7ffff7fbf071:    leave
0x7ffff7fbf072:    ret
"""

# Octets modifiés (ceux qu'on a en mémoire après le XOR)
modified = bytes([
    0xb6, 0x9e, 0xad, 0xc5,
    0x92, 0xfa, 0xdf, 0xd5,
    0xa1, 0xa8, 0xdc, 0xc7,
    0xce, 0xa4, 0x8b, 0xe1,
    0x8a, 0xa2, 0xdc, 0xe1,
    0x89, 0xfa, 0x9d, 0xd2,
    0x9a, 0xb7
])

# Clé XOR utilisée dans le shellcode (0xbeefcafe)
key = bytes.fromhex("fe ca ef be")

# On inverse
original = xor(modified, key)

print(f"[+] Bytes initiaux : {original} | ASCII : {original.decode(errors='replace')}")