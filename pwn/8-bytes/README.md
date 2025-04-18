# 8 Bytes

## Flag 
```texsaw{g0_c0m3t5!}```

## Category
pwn (easy)

## Description
I wonder how large my buffer is...

## Solution
Execute the 8_Bytes binary and observe that after being prompted for an input, the value of the variable ```secret``` is shown, as well as the value it needs to be changed to in order to get the flag

Discover that any input value longer than 8 characters will overflow the buffer and change the value of secret

From the printed value that secret needs to be changed to, use a Hex-to-ASCII tool to determine that secret needs to be set to ```WHOOOSH!```

Enter the input ```AAAAAAAAWHOOOSH!```, where the value of the 1st 8 characters can be anything, to get the flag

## Build Instructions
Use the included Makefile to run ```make```

## Downloadable Files
- 8_Bytes

## Author
sam