# precision

**Category:** Pwn  
**Challenge Name:** precision  
**Binary:** `precision`  
**Libc:** Custom provided (`libc.so.6`)  
**Tools:** pwntools, GDB, libc-database

---

## Goal

Leak the libc base address, and use it to overwrite internal libc function pointers with one-gadget RCE addresses to get a shell.

---

## How I Solved It

### 1. Leak the libc base

TO WRITE

---

You can find the full exploit script in [`main.py`](./main.py).
