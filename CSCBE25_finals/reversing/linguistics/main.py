#!/usr/bin/env python3

def c_fisher_yates_unshuffle(data):
    """
    Reverses the Fisher-Yates shuffle.
    'data' must be a multiple of 3 (3*N).
    """
    N = len(data) // 3
    swaps = [(n - 1, 0) for n in range(N, 1, -1)]  # Generate swaps
    for (posA, posB) in reversed(swaps):  # Reverse swaps
        startA, startB = posA * 3, posB * 3
        for offset in range(3):  # Swap 3-byte blocks
            data[startA + offset], data[startB + offset] = \
                data[startB + offset], data[startA + offset]
    return data

def decode_triplet(T0, T1, T2):
    """
    Decodes a triplet (T0, T1, T2) to get:
      - the original index i
      - the character bVar2
    """
    part_low = (T0 & 0xFF) - 0xE0 - 4
    c = T1 & 3
    V = T1 & 0x7F
    part_high = (V - c) >> 2
    bVar2 = (part_high << 3) + part_low
    part_i_high = (T2 & 0x3C) >> 2
    i = ((part_i_high << 2) + c) - 1
    return i, bVar2

def reverse_process(final_bytes):
    """
    Reconstructs the original array by reversing the shuffle
    and decoding triplets.
    """
    unshuffled = c_fisher_yates_unshuffle(list(final_bytes))
    N = len(unshuffled) // 3
    recovered = [None] * N
    for block_index in range(N):
        T0, T1, T2 = unshuffled[3*block_index:3*block_index+3]
        i, ch = decode_triplet(T0, T1, T2)
        recovered[i] = ch
    return recovered

if __name__ == "__main__":
    # Read the transformed data from the file and process it
    final_data = bytearray(open("secret_message.txt", "rb").read())
    original = reverse_process(final_data)
    print("Reconstructed:", original)
    print("Reconstructed (string):", "".join(chr(x) for x in original))