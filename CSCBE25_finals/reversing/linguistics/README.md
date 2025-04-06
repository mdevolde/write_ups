# linguistics

**Category:** Reversing  
**Challenge Name:** linguistics  
**Tools:** Python, custom scripts

## Goal

Recover the original secret message from a file (`secret_message.txt`) that has been transformed via a custom obfuscation process.

---

## How I Solved It

### 1. Understanding the Transformation

The challenge applies two main operations on the original message:
- **Block Shuffling:**  
  The original data is divided into 3-byte blocks. A variant of the [Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) is applied to these blocks. In order to recover the original order, my script implements a function to *reverse* the shuffle.
  
- **Triplet Decoding:**  
  Each 3-byte block (or "triplet") encodes both the original position (index) and the value of a character. Bitwise operations (masking, subtraction, and shifts) are used to extract:
  - The **original index** where the decoded character belongs.
  - The **ASCII value** (stored in a variable `bVar2`) of the character.

### 2. Reversing the Fisher-Yates Shuffle

The function `c_fisher_yates_unshuffle(data)` is designed to:
- Assume that the input data length is a multiple of 3 (i.e., there are N triplets).
- Generate the list of swap operations that were applied during the shuffle.
- Reverse these swaps (iterating in reversed order) to restore the original block order.

### 3. Decoding the Triplets

The function `decode_triplet(T0, T1, T2)` processes a single triplet by:
- Using bit masks and arithmetic to calculate two values:
  - **Index Calculation:**  
    It computes an index `i` where the recovered character should be placed.
  - **Character Extraction:**  
    It calculates `bVar2`, which represents the original ASCII value of the character.

### 4. Reconstructing the Message

The `reverse_process(final_bytes)` function ties it all together:
- **Unshuffle:**  
  It first converts the transformed byte data into a list and reverses the shuffle using the `c_fisher_yates_unshuffle` function.
- **Decode Each Block:**  
  The function then processes each 3-byte block with `decode_triplet` to obtain both the position and character.
- **Reassemble:**  
  Using the decoded index, each character is placed in the correct position of the recovered array.
- **Output:**  
  Finally, the recovered message is printed both as a list of integers and as a human-readable string.

### 5. Final Execution

The script reads the contents of `secret_message.txt`, applies the reverse process, and prints the reconstructed secret message. This allowed me to recover the original text that was obfuscated by the challenge.

---

You can find the full exploit script in [`main.py`](./main.py).
