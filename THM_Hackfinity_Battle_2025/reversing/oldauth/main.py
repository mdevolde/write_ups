#!/usr/bin/env python3

from pwn import *

# BACKTRACKING PART: FIND x[0..15] (after XOR)

def all_bytes():
    return range(256)

def backtrack_x0_to_x3():
    # x[2] = 0x51 (mandatory)
    for x0 in all_bytes():
        for x1 in all_bytes():
            for x3 in all_bytes():
                # S1 = x[0]+x[1]+x[2]+x[3] must be a multiple of 3
                s1 = x0 + x1 + 0x51 + x3
                if s1 % 3 == 0:
                    yield (x0, x1, x3)

def backtrack_x4_to_x8():
    for x4 in all_bytes():
        for x5 in all_bytes():
            for x6 in all_bytes():
                for x7 in all_bytes():
                    for x8 in all_bytes():
                        # S2 = x[4]+x[5]+x[6]+x[7]+x[8] must be a multiple of 8
                        s2 = x4 + x5 + x6 + x7 + x8
                        if s2 % 8 == 0:
                            yield (x4, x5, x6, x7, x8)

def backtrack_x9_to_x11(x8):
    # x8 is already chosen; loop over x9..x11
    for x9 in all_bytes():
        for x10 in all_bytes():
            for x11 in all_bytes():
                # S3 = x[8]+x[9]+x[10]+x[11] must be a multiple of 5
                s3 = x8 + x9 + x10 + x11
                if s3 % 5 == 0:
                    yield (x9, x10, x11)

def backtrack_x12_x14_x15():
    # x[13] = 0x34 (mandatory)
    for x12 in all_bytes():
        for x14 in all_bytes():
            for x15 in all_bytes():
                # S4 = x[12] + x[13] + x[14] + x[15] must be a multiple of 3
                s4 = x12 + 0x34 + x14 + x15
                if s4 % 3 == 0:
                    yield (x12, x14, x15)

def find_xor_array():
    """
    Finds an array x[0..15] = bytes (after XOR)
    satisfying the conditions:
      - x[2] = 0x51
      - x[13] = 0x34
      - sum(x[0..3]) % 3 == 0
      - sum(x[4..8]) % 8 == 0
      - sum(x[8..11]) % 5 == 0
      - sum(x[12..15]) % 3 == 0
    Returns the first solution found as a list of 16 integers.
    """
    x = [0]*16
    x[2] = 0x51
    x[13] = 0x34

    for (x0, x1, x3) in backtrack_x0_to_x3():
        x[0] = x0
        x[1] = x1
        x[3] = x3

        for (x4, x5, x6, x7, x8) in backtrack_x4_to_x8():
            x[4] = x4
            x[5] = x5
            x[6] = x6
            x[7] = x7
            x[8] = x8

            for (x9, x10, x11) in backtrack_x9_to_x11(x8):
                x[9]  = x9
                x[10] = x10
                x[11] = x11

                for (x12, x14, x15) in backtrack_x12_x14_x15():
                    x[12] = x12
                    x[14] = x14
                    x[15] = x15
                    # If we reach here, we have found a valid x
                    return x

    return None


def solve_key_and_username():
    """
    Finds the array x[i] = (key[i] ^ 0x52).
    Derives key[i] = x[i] ^ 0x52.
    Converts the key to hexadecimal and returns it along with the username.
    """
    x = find_xor_array()
    if x is None:
        print("No solution found :(")
        return None, None

    # Compute the plaintext key
    key_bytes = bytes([xi ^ 0x52 for xi in x])
    # Convert to hexadecimal
    key_hex = key_bytes.hex()

    # Username required by compare_with_target():
    # "elb4rt0pwn" => username[i] + 2 == target[i]
    # => username[i] = target[i] - 2
    # -> "cj`2pr.nul"
    username = "cj`2pr.nul"  

    return key_hex, username


def main():
    # Retrieve the key and the username
    key_hex, username = solve_key_and_username()
    if not key_hex or not username:
        return

    print("[*] Found key (hex)        =", key_hex)
    print("[*] Expected username      =", repr(username))

    p = process("./oldauth")

    prompt_key = p.recvuntil(b"Enter the key:").decode()
    print(prompt_key, end="")
    real_key_bytes = bytes.fromhex(key_hex)
    # Send these 16 bytes key
    p.sendline(real_key_bytes)

    prompt_user = p.recvuntil(b"Enter the username:").decode()
    print(prompt_user, end="")
    # Send the username
    p.sendline(username.encode())

    # 3) Retrieve the flag
    result = p.recvall(timeout=2).decode()
    print(result)

if __name__ == "__main__":
    main()
