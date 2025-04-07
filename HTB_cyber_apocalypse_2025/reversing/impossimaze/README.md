# impossimaze

**Category:** Reversing
**Challenge Name:** impossimaze  
**Tools:** Ghidra, `stty`

---

## Goal

Find a way to reveal the flag hidden inside a seemingly impossible maze rendered by the binary.

---

## How I Solved It

### 1. Initial behavior

When running the binary (`./main`) normally, it launches a maze-like interface in the terminal:
- A huge wall of characters is printed.
- The user can move a cursor inside the maze using keyboard inputs.
- No flag is immediately visible.

This looked like a visual puzzle or game.

---

### 2. Static analysis in Ghidra

Using Ghidra, I noticed that:
- The binary performs terminal size checks at a special point.
- It performs more visual computations when the terminal size is exactly 13 rows and 37 columns.

---

### 3. Triggering the hidden output

By matching the required terminal size using:

```bash
stty rows 13 cols 37
```

And then running the binary:
```
./main
```
...the flag appears automatically in the middle of the maze, without needing to move or solve anything manually.

---

You can find the full exploit script in [`resolve.sh`](./resolve.sh).
```
