#!/usr/bin/env python3

def quick_check(p):
    """Checks the 4 conditions of the challenge."""
    return (
        p[8] + p[3] + p[12] == 0x11B and
        p[2] + p[12] == 0xA4 and
        p[7] + p[46] == 0x8E and
        p[12] + p[32] == 0x74
    )

def brute_force_some_indices(res, indices_suspects):
    """
    Brute-forces ASCII values (32..126) at 'indices_suspects'
    to find a 'p' that satisfies quick_check.
    """
    p = list(res)  # Convert to mutable list

    def backtrack(i=0):
        """Recursive backtracking on suspect indices."""
        if i == len(indices_suspects):
            if quick_check(p):
                yield bytes(p)
            return
        idx = indices_suspects[i]
        original_val = p[idx]
        for val in range(32, 127):  # Printable ASCII
            p[idx] = val
            yield from backtrack(i + 1)
        p[idx] = original_val  # Restore original value

    for candidate in backtrack(0):
        yield candidate

def main():
    # Flag found in main.py with errors
    res_string = "csc!I_amKs0_Angry_thut_y0u_gu3ss3d_my_passw0rd!}"
    res = list(map(ord, res_string))

    # Indices to brute-force
    indices_suspects = [3, 8]

    # Search for valid candidates
    results = list(brute_force_some_indices(res, indices_suspects))
    if results:
        for r in results:
            try:
                if 'csc{' in r.decode("ascii"):
                    print(r.decode("ascii"))
            except UnicodeDecodeError:
                print(r)
    else:
        print("No valid candidates found.")

if __name__ == "__main__":
    main()