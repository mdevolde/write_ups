# endlesscycle

**Category:** Pwn / Reversing  
**Challenge Name:** endlesscycle  
**Binary:** Custom shellcode execution  
**Tools:** pwntools, static analysis, custom disassembler / debugger

---

## Goal

Analyze a dynamically generated shellcode that reads user input, XORs and compares it to an encoded flag in memory. Reverse the logic to recover the original flag.

---

## How I Solved It

### 1. Observing the shellcode

The binary executes a **dynamically generated shellcode**, starting with printing the question:

What is the flag?


This is done using a `write` syscall followed by a `read` syscall to get user input.

---

### 2. Input preprocessing

After reading user input into a buffer (`r12`), the shellcode performs:

```asm
xor dword ptr [r12], 0xbeefcafe
cmp qword ptr [r12], 0
```

It XORs the first 4 bytes with `0xBEefCAfe`, then compares them to 0.
So the correct input must be such that:
```python
input[:4] ^ 0xBEefCAfe == 0
=> input[:4] == 0xBEefCAfe
```
Meaning the first 4 bytes of input must exactly be `0xBEefCAfe`.

### 3. Comparing the rest of the flag

After that, the shellcode compares 26 more bytes of user input against an inlined string in the shellcode, using `repz cmpsb`.

However, this target string is also obfuscated, and only visible as a modified buffer in memory.

### 4. Reversing the XOR encoding

We dumped the in-memory version of the target string from the shellcode:
```python
modified = bytes([
    0xb6, 0x9e, 0xad, 0xc5,
    0x92, 0xfa, 0xdf, 0xd5,
    0xa1, 0xa8, 0xdc, 0xc7,
    0xce, 0xa4, 0x8b, 0xe1,
    0x8a, 0xa2, 0xdc, 0xe1,
    0x89, 0xfa, 0x9d, 0xd2,
    0x9a, 0xb7
])
```
We know that each of these bytes was XORed with the same key:
`0xBEefCAfe` → in bytes: `fe ca ef be` (repeating)

Using pwntools' `xor()` function, we reverse the operation:
```python
from pwn import xor

key = bytes.fromhex("fe ca ef be")
original = xor(modified, key)
```
### 5. Final flag

After decoding, we get the flag.
---

You can find the full exploit script in [`main.py`](./main.py).
