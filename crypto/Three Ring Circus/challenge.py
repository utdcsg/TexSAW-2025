#!/usr/bin/env python3
"""
Three Ring Circus - Main Challenge File
---------------------------------------

This file contains the parameters for each of the three elliptic curves.
You need to recover the secret number k that was used to generate
the public points on all three curves.
"""

import os
import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# The Three Elliptic Curves
# Curve 1: y^2 = x^3 + a1*x + b1 (mod p1)
p1 = 1019  # Modulus for curve 1
a1 = 11    # Parameter a for curve 1
b1 = 19    # Parameter b for curve 1
G1 = (712, 495)  # Base point on curve 1
P1 = (546, 929)  # P1 = k*G1

# Curve 2: y^2 = x^3 + a2*x + b2 (mod p2)
p2 = 1031  # Modulus for curve 2
a2 = 7     # Parameter a for curve 2
b2 = 13    # Parameter b for curve 2
G2 = (371, 219)  # Base point on curve 2
P2 = (150, 1019)  # P2 = k*G2

# Curve 3: y^2 = x^3 + a3*x + b3 (mod p3)
p3 = 1033  # Modulus for curve 3
a3 = 23    # Parameter a for curve 3
b3 = 11    # Parameter b for curve 3
G3 = (667, 532)  # Base point on curve 3
P3 = (480, 579)  # P3 = k*G3

# Secret key verification function
def verify_key(k):
    """Verify if the provided key is correct by checking it against the public points."""
    from utils import point_multiply

    # Verify on curve 1
    computed_P1 = point_multiply(G1, k, a1, p1)
    if computed_P1 != P1:
        return False

    # Verify on curve 2
    computed_P2 = point_multiply(G2, k, a2, p2)
    if computed_P2 != P2:
        return False

    # Verify on curve 3
    computed_P3 = point_multiply(G3, k, a3, p3)
    if computed_P3 != P3:
        return False

    return True

# Decrypt the message function
def decrypt_message(key_int):
    """Decrypt the message to find the flag."""
    try:
        # Convert int key to bytes
        key_hex = format(key_int, 'x').zfill(32)
        key = bytes.fromhex(key_hex)[:16]  # Use first 16 bytes as AES key
        
        # Read the encrypted file
        with open('encrypted_message.bin', 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()
        
        # Decrypt
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), 16)
        
        return plaintext.decode('utf-8')
    except Exception as e:
        return f"Decryption failed: {e}"

if __name__ == "__main__":
    print("=" * 60)
    print("Three Ring Circus - Cryptographic Challenge")
    print("=" * 60)
    print("To solve this challenge, you need to:")
    print("1. Find the order of each base point G1, G2, and G3")
    print("2. Solve the discrete logarithm problem for each curve")
    print("3. Use the Chinese Remainder Theorem to find the secret key k")
    print("4. Use the recovered k to decrypt the message and find the flag")
    print("=" * 60)
    
    try:
        key = int(input("Enter the secret key (decimal integer): "))
        
        print("\nVerifying key across all three curves...")
        if verify_key(key):
            print("Key verification successful!")
            print("\nDecrypting message...")
            plaintext = decrypt_message(key)
            print(f"\nDecrypted message: {plaintext}")
        else:
            print("Key verification failed. The key is incorrect.")
    except ValueError:
        print("Invalid input. Please enter a decimal integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
