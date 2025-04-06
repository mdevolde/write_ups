# getflag

**Category:** Pwn  
**Challenge Name:** permission denied  
**Tools:** pwntools, gdb

## Goal

The goal of this challenge is to exploit a binary that decreases privileges using `seteuid` and makes the stack executable. The binary prompts for a password, making a buffer overflow possible. The challenge is to gain root access and retrieve the flag.

## How I solved it

1. **Initial analysis**  
   The binary prompts:
   ```
   Give the password at 0xdeadbeef if you have the permission to see my secret...
   ```
   The address (`0xdeadbeef` here) is dynamically provided at runtime. This value corresponds to a stack address we can control.

   By performing some reverse engineering, we observe the following:
   - In the initialization function, the stack is made executable (which is not the default behavior, as confirmed by `checksec`).
   - The binary's privileges are dropped using `seteuid`, which explains the need to regain them later in the exploit.

2. **Stack address leak**  
We read the line up to `Give the password at ` and capture the next 14 characters to extract the leaked stack address. This gives us a reference point to place our shellcode.

3. **Shellcode setup**  
I crafted a shellcode that:
- First, performs a syscall `setuid(0)` to regain root privileges that were dropped at the start of the binary using `seteuid`.
- Then executes a standard `/bin//sh` shell-spawning syscall (execve).

4. **Placing the shellcode**  
The binary likely has a buffer of 56 bytes before the return address (based on testing or reverse engineering). So the shellcode goes first, padded with NOPs to fill up to 56 bytes.

5. **Return address overwrite**  
I then overwrite the return address with a pointer into the middle of my payload — exactly 20 bytes before the leaked stack address. This ensures that when the function returns, it jumps to my shellcode.
The overwritten return address is an address found by checking the program's backtrace with gdb (past-main).

6. **Sending the payload**  
The payload is sent after the message:  
_"if you have the permission to see my secret..."_

7. **Shell obtained**  
Once the payload is delivered, I get a shell. From there, I can retrieve the flag.

---

You can find the exploit script in [`main.py`](./main.py).

