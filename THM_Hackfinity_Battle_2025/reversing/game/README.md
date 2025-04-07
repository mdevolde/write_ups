# game

**Category:** Reversing  
**Challenge Name:** game  
**Tools:** `strings`, `grep`

---

## Goal

Find the flag hidden inside the binary `Tetrix.exe`.

---

## How I Solved It

### 1. Static analysis

Since the binary is a Windows executable, I began with a **quick static scan** to search for any embedded flag or readable string.

Using the command:

```bash
strings ./Tetrix.exe | grep THM
```
...I filtered all printable strings for the common flag prefix used in the CTF (`THM{...}`).

### 2. Result

The flag was embedded directly in the binary and printed out by strings, without requiring reverse engineering or debugging.

---

You can find the full exploit script in [`soluce.sh`](./soluce.sh).
