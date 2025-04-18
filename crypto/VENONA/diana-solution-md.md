# DIANA Cipher Solution - TeXSAW CTF Challenge

## Challenge Overview

The challenge presents a cryptography scenario where we're examining encrypted messages from an abandoned intelligence outpost in Vietnam. We're given:

1. A reference table for the DIANA cipher (in the image "DIANA.tiff")
2. Two plaintext messages
3. Three encrypted messages

We need to determine which of the encrypted messages contains critical information (the flag).

## The DIANA Cipher

The DIANA cipher is a polyalphabetic substitution cipher similar to a Vigenère cipher but using a different tabular arrangement. Each letter of the key specifies which substitution alphabet to use for each corresponding letter of the plaintext.

### How the DIANA Cipher Works:

1. **The Table**: The DIANA table consists of 26 rows (one for each letter of the alphabet). For each row:
   - The top row is the standard alphabet (A-Z)
   - The bottom row is a shifted version of the alphabet, with each row having a different shift

2. **Encryption Process**:
   - For each letter in the plaintext, use the corresponding letter from the key to select which row of the table to use
   - Find the plaintext letter in the top row of that key letter's row
   - Replace it with the corresponding letter from the bottom row

3. **Decryption Process**:
   - For each letter in the ciphertext, use the corresponding letter from the key to select which row of the table to use
   - Find the ciphertext letter in the bottom row of that key letter's row
   - Replace it with the corresponding letter from the top row

## Solution Approach

1. **Known Plaintext Attack**: Since we have both plaintext and ciphertext messages, we can attempt to determine the key used for encryption.

2. **Key Discovery**:
   - For each plaintext-ciphertext pair, we compute the key that would map each plaintext character to its corresponding ciphertext character
   - We analyze the derived key to identify repeating patterns, which would indicate the true key length
   - A repetitive pattern suggests the key is cyclical (e.g., "ABCABC" indicates a key of "ABC" repeated)

3. **Finding the Correct Key**:
   - By trying each plaintext with each ciphertext, we identified a common key pattern: "RWLMBZTCVFQPAYHGXKNSOEDIUJ"
   - This key successfully decrypts both known plaintext messages when applied to their respective ciphertexts

4. **Decrypting the Third Message**:
   - Using the discovered key, we decrypt the third encrypted message to reveal:
   "THEFLAGISWONTIMEPADWITHUNDERSCORESBETWEENWORDSWRAPPEDINTHEHEADER"

5. **Extracting the Flag**:
   - Following the flag format instructions, we get: texsaw{won_time_pad}

## Key Insights

The DIANA cipher appears secure, but has a critical weakness when the same key is reused for multiple messages (similar to a one-time pad that's used more than once). This allowed us to perform a known-plaintext attack and recover the key.

The name "DIANA" and the flag "won_time_pad" both reference the one-time pad encryption method, which is theoretically unbreakable if used correctly (with a truly random key that's never reused). However, when the "one-time" rule is violated, the cipher becomes vulnerable - hence "won" (meaning "one" but used multiple times).

## Implementation Details

The solution uses three main functions:

1. `create_diana_table()`: Constructs the DIANA cipher table based on alphabet rotations
2. `decrypt_diana()`: Decrypts a message using the DIANA cipher given a key
3. `find_key_from_known_text()`: Discovers the encryption key by analyzing known plaintext-ciphertext pairs

The program then analyzes all combinations of plaintext and ciphertext messages to identify the key, uses it to decrypt all three messages, and reveals the flag.
