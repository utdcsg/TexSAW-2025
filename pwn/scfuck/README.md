# scfuck

Get arbitrary code execution in C with 5 or fewer unique characters when the data section is executable.

# Author

caandt

# Category

pwn (easy)

# Description

this is not a c challenge

# Flag

`texsaw{it_was_a_b_challenge...}`

# Solution

The linker script used makes the data section executable. We can put arbitrary bytes into the data section with the character set `b01=;` by using binary literals. To solve the challenge, put shellcode into the data section and define `main` to be the first variable used to execute it.
