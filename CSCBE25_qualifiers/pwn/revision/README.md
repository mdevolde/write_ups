# revision

**Category:** Pwn  
**Challenge Name:** revision  
**Binary:** `revision`  
**Tools:** pwntools, Ghidra, gdb  

## Goal

Exploit a buffer overflow to call a hidden function with two specific arguments, and retrieve the flag.

---

## How I Solved It

### 1. Analyzing the binary

Static analysis revealed a classic setup:
- The binary defines a hidden function at address `0x080491b6`.
- This function expects **two integer arguments**.
- There is a vulnerable `gets()` call that allows overflowing a local buffer on the stack.

Using tools like `Ghidra`, I confirmed:
- The function takes two arguments.
- There is a buffer of 32 bytes, followed by the return address, and then the EBP.

---

### 2. Building the exploit

I created the payload in this structure:

[a * 32] + [RET address] + [fake EBP or junk] + [arg1] + [arg2]


More precisely:

```python
payload  = b"a" * 32                     # buffer padding
payload += p32(0x080491b6)               # address of target function
payload += b"JUNK"                       # placeholder for EBP (4 bytes)
payload += p32(0xDEADBEEF)               # first argument
payload += p32(0xCAFEBABE)               # second argument
```

This uses the standard 32-bit calling convention:
- Arguments are pushed after the return address.

### 3. Sending the payload

Using pwntools:

```python
p = process("./revision")
p.sendline(payload)
``` 

After sending the payload, the binary executed the function 0x080491b6 with the correct arguments, and printed the flag.

### 4. Result

The flag is printed directly by the called function. The exploit doesn't need to leak or read memory.

---

You can find the full exploit script in [`main.py`](./main.py).
