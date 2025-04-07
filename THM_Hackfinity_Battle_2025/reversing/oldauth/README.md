# oldauth

**Category:** Reversing  
**Challenge Name:** oldauth  
**Binary:** `oldauth`  
**Tools:** Python, pwntools, custom solver (brute-force/backtracking)

---

## Goal

Recover a 16-byte authentication key and a valid username that satisfy custom verification constraints enforced by the binary. Submit both to get the flag.

---

## How I Solved It

### 1. Understanding the logic

Static analysis revealed that:
- A 16-byte **key** is read and XOR’d with `0x52`.
- The resulting values (let's call them `x[i] = key[i] ^ 0x52`) are passed through multiple **modulo-based constraints**:

| Bytes involved         | Constraint                                  |
|------------------------|---------------------------------------------|
| `x[0] + x[1] + x[2] + x[3]` | Must be divisible by 3                   |
| `x[4] + x[5] + x[6] + x[7] + x[8]` | Must be divisible by 8         |
| `x[8] + x[9] + x[10] + x[11]` | Must be divisible by 5                |
| `x[12] + x[13] + x[14] + x[15]` | Must be divisible by 3              |
| `x[2] = 0x51` and `x[13] = 0x34` | Hardcoded constraints              |

These constraints form a complex search space, so I wrote a backtracking algorithm to find a valid set of values for `x[0]..x[15]`.

---

### 2. Reconstructing the key

Once a valid `x[0..15]` array was found, I applied the inverse XOR:

```python
key[i] = x[i] ^ 0x52
```

This gave me the correct 16-byte binary key, ready to be sent to the program.

### 3. Username logic

A secondary check required a valid username where:
```python
target[i] == username[i] + 2
```

The original code used "elb4rt0pwn" as the target so I reversed it:
```python
username = ''.join(chr(ord(c) - 2) for c in "elb4rt0pwn")  # → "cj`2pr.nul"
```
### 4. Final exploit

The script connects to the binary, and:
- Sends the raw binary key (16 bytes)
- Sends the correct username
- Receives and prints the flag

```python
p.sendline(real_key_bytes)     # binary key
p.sendline(username.encode())  # "cj`2pr.nul"
```

---

You can find the full exploit script in [`main.py`](./main.py).
