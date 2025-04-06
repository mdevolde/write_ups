# myrpg1

**Category:** Pwn  
**Challenge Name:** myrpg1 
**Tools:** pwntools, GDB, Ghidra

---

## Goal

Exploit a buffer overflow in a roleplay-like binary to execute shellcode and spawn a shell.

---

## How I Solved It

### 1. Initial analysis

The binary is a 64-bit ELF with a menu-driven interface, imitating a simple RPG.
Here is some interesting observations:
- *left entrance* contains a memory leak of an address.
- *talk* contains a buffer overflow.

### 2. Leaking a stack address

Using option `2` after starting a new game, the binary leaks an address:

```text
[DEBUG] dialogue address : 0x7ffc6a0f3f40
``` 

This is the address of a buffer that we can later overwrite. It's crucial for us to redirect execution to our injected shellcode.

### 3. Crafting shellcode

I wrote a 64-bit shellcode that spawns `/bin//sh`. It includes:
- A `mov` to place `/bin//sh on` the stack
- Register setup (`rdi`, `rsi`, `rdx`) for `execve`
- A `syscall` instruction (`syscall` with `rax = 59`)

```asm
and rsp, 0xFFFFFFFFFFFFFFF0
sub rsp, 0x40
mov rax, 0x68732f6e69622f2f
mov [rsp], rax
mov byte [rsp+7], 0
...
syscall
```

### 4. Buffer overflow

The vulnerable function `talk` reads user input into a buffer of 56 bytes without bounds checking.

I built the payload as follows:
- A NOP sled
- The shellcode
- The leaked address as the return address (so that execution jumps into our shellcode)

```python
payload  = b"\x90" * (56 - len(shellcode))
payload += shellcode
payload += p64(leaked_addr)
```

### 5. Exploit flow

The full interaction:
- Start a new game
- Use the left entrance to leak the stack address
- Start a new game again
- Use talk to send the overflow payload
- Exit the cave to trigger the return and jump to shellcode

#### 6. Result

After the payload is sent and we exit the cave, we get an interactive shell.

---

You can find the full exploit script in [`main.py`](./main.py).