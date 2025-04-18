## Flag
Flag: texsaw{n0T_s3crEt_p4sSword}

## Intended Way to Solve
Pull up the binary in Ghidra, scroll through the code to get to the verify_password section.
From the last loop in the verify_password section, you can see that there's an 
XOR operation going on between two of the variable arrays; the variable arrays are
in hex and have 19 terms each. Copy and paste those variables into
Cyberchef to first convert one of the variables from hex, and then perform the XOR
operation.

Order in Cyberchef:
From hex (input is one of the variables)
Xor (with the key being the other variable)

Or, using whatever tool, just XOR the two variable arrays with 19 elements
and then convert from hex.

## Setup Instructions
Only post the binary
To get the binary: gcc -o main.c main

## Downloadable code
main
