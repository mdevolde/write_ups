# prospectors_claim

**Category:** Reversing
**Challenge Name:** prospectors claim  
**Tools:** Z3 (Python bindings), Regex, ghidra

---

## Goal

Recover a 64-byte flag that satisfies a large set of boolean conditions hardcoded in a binary. The flag is checked via a massive number of `if` statements that manipulate stack values and compare, xor, or add bytes together.

---

## Reverse Engineering

### 0. First analysys

The binary contained hundreds of conditions of the form:

```c
if (local_42 == 0x36) { bump(0,&score); }
if ((local_3a ^ local_3f) == 0x53) { bump(0,&score); }
if ((byte)(local_1a + local_31) == -0x7f) { bump(0,&score); }
```

Each of these conditions tested whether certain relationships held between values stored in stack-local variables like `local_3a`, `local_1f`, etc.

Each condition awarded one point to a score variable when satisfied.

### 1. Strategy

Instead of trying to solve this manually (or even with dynamic analysis), I decided to:
- Parse all the constraints using regular expressions.
- Symbolically model the 64 variables using BitVec(8) objects in Z3.
- Add constraints to Z3 in a Max-SAT fashion:
- Each constraint is added as a soft constraint with equal weight.
- Z3 attempts to maximize the number of satisfied constraints.

I also fixed the known prefix of the flag (`PCTF{`) by hardcoding:
```python
vars_z3[0] == ord('P')
vars_z3[1] == ord('C')
vars_z3[2] == ord('T')
vars_z3[3] == ord('F')
vars_z3[4] == ord('{')
```
### 2. Constraints Handled

The parser supports four types of constraints:
- Equality: local_X == constant
- Variable equality: local_X == local_Y
- XOR: (local_X ^ local_Y) == constant
- Byte addition: ((local_X + local_Y) & 0xFF) == constant

Some edge cases (e.g., negated values or exotic encodings) are normalized to fit this model.

### 3. Solving

Using Z3’s `Optimize()`, I launched a `Max-SAT` query with a timeout, and I found the flag.

---

You can find the full exploit script in [`main.py`](./main.py).
