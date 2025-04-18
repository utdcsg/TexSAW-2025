# String Symphony

## Category
Pwn - Medium

## Description
Explore an abandoned tower that holds mystic secrets. Can you teleport into the abyss to find the path to achieving godly powers? 

## Solution
Solution: The user should decompile the program and find that they need to enter “runestone” when interacting with the wishing stone. This allows interaction with an array. The user is expected to find the index to where the “floor” variable is stored on the stack and overwrite it with a specific value (found through examining variables in GDB or a decompiler) that will take the user to a secret floor with a buffer overflow opportunity. This buffer overflow should be exploited to construct a ROP chain that allows the user to return to libc and call system() with the "/bin/sh" string in libc to open a shell.

## Flag
texsaw{n0cl1pp1ng_1nt0_th3_4str4l_r34lm_g1v3s_y0u_d1v1n3_p0w3rs}

## Downloadable
chall  

## Setup
Build the challenge binary from the Makefile and source file (see below).  
Make sure the Dockerfile, compose.yml, flag.txt, and binary are in the same directory.  
Run "sudo docker compose build"  
Run "sudo docker compose up"  
The user can now connect to the challenge Docker container using nc.

## Building Binaries
Have the Makefile and .c file in the same directory, and run "make".