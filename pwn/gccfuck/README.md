# gccfuck

Get arbitrary code execution in C (GCC 13.3.0) with 12 or fewer unique characters.

# Author

caandt

# Category

pwn (hard)

# Description

c is twice as hard as javascript so i gave you twice as many characters

# Flag

`texsaw{wtf_is_a_modular_multiplicative_inverse}`

# Solution

todo: better writeup

1. enable executable stack with gcc nested function
2. define enough functions to get constants in the 0x401xxx range
3. multiply the function addresses to get shellcode bytes (see mod_mult.py)
4. write shellcode to stack and call with function pointer
5. profit
