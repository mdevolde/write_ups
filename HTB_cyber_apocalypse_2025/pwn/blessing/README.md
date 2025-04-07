# blessing

**Category:** Pwn  
**Challenge Name:** blessing  
**Binary:** `blessing`  
**Tools:** pwntools, GDB, Ghidra, hooks (`usleep.so`, `sleep.so`)

---

## Goal

Abuse an integer sign mismatch vulnerability to write outside of a buffer and hijack control flow.

---

## How I Solved It

### 1. Analyzing the binary

When starting the binary, it prints a message like:

Please accept this: `0x7fffffffe310`


This is the stack address of a local buffer (`local_20`). The binary then prompts:

- `Give me the song's length:` (expects a signed integer)
- `Tell me the song:` (reads that many bytes into a buffer)

**Key vulnerability:**  
Internally, the buffer length is checked with a signed comparison, but passed to a function `read()` that interprets it as **unsigned** — causing potential buffer overflow.

`*(undefined8 *)((long)local_18 + (local_30 - 1)) = 0;`
This line is crucial as it sets the last byte of the buffer to `0`, which is a common technique to null-terminate strings in C. However, if the length is negative, it can lead to writing outside the bounds of the allocated buffer.

---

### 2. The vulnerability

If you pass a **negative signed integer**, it gets cast to a **large unsigned value** — effectively bypassing any bounds checking and allowing writing far beyond the buffer.

The goal is to **set 0 at local_20 address** and so enter to the `read_flag()` function. 

---

### 3. Strategy

We know the address of `local_20`, and we can manipulate our input to be negative and so, the vulnerable line will write 0 at `local_20`:

To pass it through the program, we must send it as a signed 64-bit integer, even if it's interpreted as unsigned inside:

```python
def to_signed(val, bits=64):
    if val & (1 << (bits - 1)):
        return val - (1 << bits)
    return val
```

### 4. Payload

We send the manipulated length:
```python
p.sendline(str(malicious_signed_addr).encode())
p.sendline(b"garbage")
```

This causes the program to write too far into the stack, specifically at the address of `local_20`, which is where we want to write `0`.

### 5. Result

After sending the payload, the binary prints the flag:

---

You can find the full exploit script in [`main.py`](./main.py).
