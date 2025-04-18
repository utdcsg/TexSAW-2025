# Three Ring Circus

Are you a Crypto Clown?

## Challenge Files

This package contains the following files:

- `challenge.py`: The main challenge file containing the elliptic curve parameters and verification functions. Run this file to test your solution.
- `utils.py`: Utility functions for elliptic curve operations. Some functions are incomplete and need to be implemented to solve the challenge.
- `encrypted_message.bin`: An encrypted file containing the flag. You'll need to recover the secret key to decrypt this file.
- `generate_encrypted_message.py`: (For challenge creators only) Script to generate the encrypted message file with the flag.

## Solution Files (Private)

These files should not be distributed to participants:

- `solution/solution.py`: Complete implementation that solves the challenge.
- `solution/SOLUTION_GUIDE.md`: Detailed explanation of the solution approach and mathematical concepts.

## Objective

Solve the elliptic curve discrete logarithm problem across three different elliptic curves, then use the Chinese Remainder Theorem to find the secret key. Use the key to decrypt the message and find the flag.

Flag format: texsaw{FLAG}
