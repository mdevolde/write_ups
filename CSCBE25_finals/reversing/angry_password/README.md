# angry_password

**Category:** Reversing  
**Challenge Name:** angry_password  
**Tools:** Python (custom scripts)

## Goal

Recover a 48-byte password that passes an integrity check and reveals the flag.

---

## How I solved it

### 1. Understanding the challenge

The binary performs a **byte-wise transformation** on the user input and checks that the final array matches a hardcoded array of 48 bytes (`local_68`). The actual password is transformed *before* being compared, so we need to **reverse** this transformation.

---

### 2. Reverse engineering the transformation

The transformation logic was XOR-based and applied in-place. Fortunately, the operation is symmetric, which allows us to reverse it.

I reimplemented the inverse logic in Python:

```python
def inverse_transform(final_bytes):
    arr = final_bytes[:]
    length = len(arr)
    for c in reversed(range(length)):
        iVar3 = (4 + 14 * c) % length
        arr[c] = arr[c] ^ arr[iVar3] ^ arr[(9 + iVar3 * c) % length]
    return arr
```

Using this on the local_68 array gives us a candidate password.

### 3. Quick check validation

The binary includes a `quick_check` function which verifies 4 conditions on specific byte indices:

```python
p[8] + p[3] + p[12] == 0x11B
p[2] + p[12]         == 0xA4
p[7] + p[46]         == 0x8E
p[12] + p[32]        == 0x74
``` 
After reversing the transformation, I found that the resulting string almost looked like a flag, but some characters were incorrect. So, I assumed a few bytes were wrong and needed to be corrected manually.

### 4. Targeted brute-force on suspicious bytes

To avoid brute-forcing the entire 48-byte password (which would be infeasible), I focused only on a few "suspicious" indices — the ones that seemed visually wrong in the candidate string (e.g., lowercase `csc!` instead of uppercase `CSC{`).

I wrote a backtracking brute-force function to test all ASCII-printable values at those positions, and only kept results that passed the `quick_check`.

---

The two scripts are available in [main.py](./main.py) and [correct.py](./correct.py).
