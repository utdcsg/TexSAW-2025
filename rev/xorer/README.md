# XORer

## Flag 
```texsaw{n0t_th3_fl4g}```

## Category
rev (easy)

## Description
I wonder what should be XORed with what...

## Solution
Execute the XORer binary and observe that after being prompted for an input, no other helpful output is printed besides ```Wrong password!```

Use a decompiler to discover that each byte of the input is XORed with the value ```A5``` and then compared to a hard-coded value. If the correct sequence of XORed values are entered, then the flag is printed

Copy the hard-coded value and use any tool to XOR each byte with the value ```A5``` to obtain the password ```n0t_th3_fl4g```

Execute the XORer binary again and enter the password to get the flag

## Build Instructions
Use the included Makefile to run ```make```

## Downloadable Files
- XORer

## Author
sam