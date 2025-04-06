# programming - meme obfuscation

**Category:** Programming  
**Challenge Name:** Shakespearean Poem  
**Tools:** Python  

## Goal

Decrypt a message (`secret.txt`) that has been obfuscated using an absurdly named series of meme-themed functions. The challenge is written in a parody dialect of Python and needs to be deciphered and executed correctly to retrieve the original message.

---

## How I Solved It

### 1. Translating the "language"

The original source was a distorted pseudo-Python with Gen Z slang:
- `bop` instead of `def`
- `meowing ... diddy ...` instead of standard list comprehensions
- `its giving` instead of `return`
- `huzz` instead of `range`
- Useless or weird function names (`W`, `Boujee`, `High_Key`, etc.)

I manually cleaned up the syntax to standard Python 3 to be able to run and debug the code.

---

### 2. Analyzing the logic

The program revolves around:
- A decryption function: `Glow_Up(data, key)` → simple XOR with the key
- A key transformation pipeline consisting of many obfuscated steps:
  
The transformation path for the key is:

```python
key = "supersecretkey"
key = [ord(k) for k in key]
key = Salty(key)                        # chain of small transformations
key = E_boy_or_E_girl(key)             # XOR with 42
Stan(key)                              # sum(key) % 256, not used later
key = Big_Yikes(key)                   # x * 2
key = Ghosting(key, 5)                 # +5 modulo 256
key = Fam(key)                         # reverse
key = W(key)                           # swap adjacent bytes
key = W(key)                           # swap again
key = Fam(key)                         # reverse back
key = Ghosting(key, -5)                # reverse previous +5
key = Cheugy(key)                      # XOR with 99
key = High_Key(key)                    # 10x repeat: x*7 mod 256
key = [x + 1 for x in key]
key = [x // 2 for x in key]
```

The key goes through many small reversible or lossy transformations to obfuscate the actual XOR key used in `Glow_Up`.

### 3. Fixing and running the program

I fixed the broken syntax and ran the corrected version on the provided `secret.txt` file, which contained the encrypted message.

The corrected `Glow_Up()` decrypted the message using the transformed key, and printed out the flag.

---

The transfored code is available in [shakespearean_poem_fixed.py](./shakespearean_poem_fixed.py). 
