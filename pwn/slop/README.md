# slop

Get arbitrary code execution by passing arguments to the linker.

# Author

caandt

# Category

pwn (medium/hard)

# Description

can we please get some actual pwn instead of this slop over and over again

# Flag

`texsaw{i_hope_you_enjoyed_Some_Linker_Oriented_Programming}`

# Solution

Statically link libc into binary, set the entry point address, and chain together "LOP" gadgets (sequence of instructions ending with a `call` to a symbol that can be set through `--defsym`) to get a shell.
