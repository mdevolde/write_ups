# Ruby FLAG Editor

**Category:** Programming  
**Challenge Name:** Spelling Rubee

## Goal

The goal of this challenge is to write a Ruby program that prints the value of the `FLAG` variable. The challenge is designed to be solved by building the program one character at a time, with the restriction that the program must be valid Ruby code at each step.

## How I solved it

1. The challenge starts by letting you build a Ruby program one character at a time.
2. I chose `p` as the first character — this is the start of `puts` or `p`, both valid ways to print in Ruby.
3. The interface allows only modifying the last line, so I had to be creative:
   - I first built a line with `p`
   - Then a character in the line with just `p ` (with a space)
   - Then I added a comment to the line with `#` to make it a valid Ruby program. `p #`
   - Then, I added the `FLAG` variable to the line. `p #FLAG`
   - Finally, I removed the comment to make it a valid Ruby program. `p FLAG`

This program prints the value of the `FLAG` variable, which is the flag for this challenge.

---

You can check the output in [output.txt](./output.txt).
