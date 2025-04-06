# Apple Pie

**Category:** Reversing  
**Challenge Name:** Apple Pie  
**Tools:** Python (custom scripts)

## Goal

Reverse a simple character-level encoding using a static mapping table, in order to recover the original secret string.

---

## How I Solved It

### 1. Static analysis of the binary

Upon disassembling the binary, I noticed a very straightforward transformation:
- A constant array of bytes (integers between 0 and 9) is used to modify each character of the secret string.
- The transformation follows this logic:

```python
for i, char in enumerate(secret):
    encoded_char = ord(char) + MAPPING_TABLE[i]
``` 

This is a simple additive substitution cipher with a static table, meaning we can easily reverse it by subtracting the same values.

### 2. Rewriting the decoder

I reconstructed the original encoding logic in Python and wrote the inverse:

```python 
def pie_decode_secret(encoded):
    decoded_chars = []
    for i, char in enumerate(encoded):
        decoded_chars.append(chr(ord(char) - MAPPING_TABLE[i]))
    return "".join(decoded_chars)
``` 

There were a couple of characters that didn't decode properly due to minor encoding issues, so I applied manual replacements:
```python 
.replace("¹", "y").replace("¾", "}")
``` 

This fixed the last discrepancies in the output.

### 3. Result

Using the encoded string found in the binary:
```python 
"ftg|rÂalfytzr{nbrlmcoueessthaj{zmdtmÂ"
``` 
The script returned:

Decoded Secret: `CSC{...}` 

(The full flag is revealed at runtime after decoding.)

---

You can find the full exploit script in [`main.py`](./main.py).
