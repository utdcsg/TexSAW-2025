#!/usr/bin/env python3
"""
Generate the encrypted message file for the Three Ring Circus challenge.
This is for challenge creators only and should not be distributed to participants.
"""

import os
import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# The secret key value (this is what participants need to find)
SECRET_KEY = 29478365012847596

# The flag is now hardcoded
flag = "texsaw{Crypt0_M4g1c14n}"

# The plaintext message
plaintext = f"""
=====================================================
THREE RING CIRCUS - FLAG
=====================================================

Congratulations on solving the cryptographic challenge!

Flag: {flag}

=====================================================
"""

# Convert key to bytes for AES
key_hex = format(SECRET_KEY, 'x').zfill(32)
key = bytes.fromhex(key_hex)[:16]  # Use first 16 bytes as AES key

# Generate random IV
iv = os.urandom(16)

# Encrypt the plaintext
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), 16))

# Write the encrypted file
with open('encrypted_message.bin', 'wb') as f:
    f.write(iv)
    f.write(ciphertext)

print(f"Encrypted message file generated!")
print(f"Secret key: {SECRET_KEY}")
print(f"Flag: {flag}")
