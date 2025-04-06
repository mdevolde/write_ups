#!/usr/bin/env python3

def quick_check(p):
    """Checks the 4 conditions of the challenge."""
    return (
        p[8] + p[3] + p[12] == 0x11B and
        p[2] + p[12] == 0xA4 and
        p[7] + p[46] == 0x8E and
        p[12] + p[32] == 0x74
    )

def inverse_transform(final_bytes):
    """Reverses the transformation to get the initial array."""
    arr = final_bytes[:]
    length = len(arr)
    for c in reversed(range(length)):
        iVar3 = (4 + 14 * c) % length
        arr[c] ^= arr[iVar3] ^ arr[(9 + iVar3 * c) % length]
    return arr

def main():
    # Local array from validate
    local_68 = [
        0x59, 0x60, 0x25, 0x21, 0x7B, 0x30, 0x61, 0x2D,
        0x4B, 0x4B, 0x22, 0x50, 0x7F, 0x7E, 0x59, 0x0C,
        0x4B, 0x4A, 0x74, 0x3A, 0x66, 0x31, 0x24, 0x33,
        0x00, 0x66, 0x0A, 0x67, 0x41, 0x09, 0x4B, 0x33,
        0x33, 0x5C, 0x4D, 0x0E, 0x73, 0x4F, 0x5D, 0x64,
        0x4B, 0x66, 0x77, 0x5A, 0x66, 0x21, 0x6A, 0x1A
    ]
    
    # Reverse transformation
    original = inverse_transform(local_68)
    
    # Check quick_check
    if quick_check(original):
        print("[+] quick_check OK!")
    else:
        print("[-] quick_check FAILED.")
    
    # Display password
    print("Password (in ASCII) = ", "".join(chr(x) for x in original))

if __name__ == "__main__":
    main()

