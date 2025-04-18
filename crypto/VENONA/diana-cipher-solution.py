"""
DIANA Cipher Solution - TeXSAW CTF Challenge
"""

def create_diana_table():
    """Create the DIANA cipher table mapping each letter to a shifted alphabet"""
    diana_table = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i, letter in enumerate(alphabet):
        # Create shifted alphabet for each letter
        offset = 26 - i
        shifted_alphabet = alphabet[-offset:] + alphabet[:-offset]
        diana_table[letter] = shifted_alphabet
    
    return diana_table

def decrypt_diana(ciphertext, key, diana_table):
    """
    Decrypt a message encrypted with the DIANA cipher
    
    Args:
        ciphertext (str): The encrypted message
        key (str): The encryption key
        diana_table (dict): DIANA cipher table
        
    Returns:
        str: The decrypted message
    """
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Remove non-alphabetic characters from ciphertext
    ciphertext = ''.join(c for c in ciphertext if c.isalpha()).upper()
    
    for i, char in enumerate(ciphertext):
        # Get the key character for this position (repeating the key as needed)
        key_char = key[i % key_length]
        
        # Get the shifted alphabet for this key character
        shifted_alphabet = diana_table[key_char]
        
        # Find the position of the ciphertext character in the shifted alphabet
        pos = shifted_alphabet.index(char)
        
        # Map back to the standard alphabet
        plaintext += alphabet[pos]
            
    return plaintext

def find_key_from_known_text(ciphertext, known_plaintext, diana_table):
    """
    Find the encryption key using known plaintext-ciphertext pairs
    
    Args:
        ciphertext (str): The encrypted message
        known_plaintext (str): The known plaintext
        diana_table (dict): The DIANA cipher table
        
    Returns:
        str: The potential key
    """
    # Clean up the texts - remove non-alphabetic characters and convert to uppercase
    ciphertext = ''.join(c for c in ciphertext if c.isalpha()).upper()
    known_plaintext = ''.join(c for c in known_plaintext if c.isalpha()).upper()
    
    # Use only the length of the shorter text
    length = min(len(ciphertext), len(known_plaintext))
    ciphertext = ciphertext[:length]
    known_plaintext = known_plaintext[:length]
    
    potential_key = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # For each character pair, determine which key letter would map plaintext to ciphertext
    for i in range(length):
        p_char = known_plaintext[i]
        c_char = ciphertext[i]
        
        # Find which key row would map p_char to c_char
        for key_char in alphabet:
            bottom_row = diana_table[key_char]
            if bottom_row[alphabet.index(p_char)] == c_char:
                potential_key += key_char
                break
    
    # Look for repeating patterns in the key
    for key_length in range(2, 20):  # Try keys of length 2 to 19
        if len(potential_key) >= key_length * 2:
            repeat = True
            base_key = potential_key[:key_length]
            
            # Check if this segment repeats
            for i in range(key_length, len(potential_key), key_length):
                segment = potential_key[i:i+key_length]
                if segment and segment != base_key[:len(segment)]:
                    repeat = False
                    break
            
            if repeat:
                return base_key
    
    return potential_key

def main():
    # Create the DIANA cipher table
    diana_table = create_diana_table()
    
    # Load the encrypted messages
    encrypted_messages = [
        "RCPZURNPAQELEPJUJZEGAMVMXWVWCTBMHKNYEEAZVXQWVKGMRVWXDLCANHLGY",
        "FLPDBSBQIGBJECHMIOZGJMQONXJANFPQYQPWIIONYKNERKHIABLJTPTAOZMDGZUTAESK",
        "KDPRMZZKNBECTGTKMKQOWXKCHMVNDOPQXUWJJLECUCLBQKKVDXJNUEYFIDAGVIUG"
    ]
    
    # Known plaintext messages
    plaintext_messages = [
        "OPERATION BLUE EAGLE MOVING TO SECTOR FOUR STOP REQUEST EXTRACTION AT BLUE EAGLE",
        "AGENT SUNFLOWER COMPROMISED NEAR HANOI STOP ABORT MISSION COMPROMISED"
    ]
    
    print("=== ATTEMPTING TO FIND THE KEY ===")
    
    # Try to find the key from the known plaintext/ciphertext pairs
    for i, plaintext in enumerate(plaintext_messages):
        for j, ciphertext in enumerate(encrypted_messages):
            potential_key = find_key_from_known_text(ciphertext, plaintext, diana_table)
            
            print(f"Plaintext {i+1} with Ciphertext {j+1} suggests key: {potential_key}")
            
            # Test the key by decrypting the ciphertext
            decrypted = decrypt_diana(ciphertext, potential_key, diana_table)
            print(f"Decryption with this key: {decrypted[:50]}...\n")
    
    # The key discovered from analysis: RWLMBZTCVFQPAYHGXKNSOE...
    discovered_key = "RWLMBZTCVFQPAYHGXKNSOEDIUJ"
    
    print("=== DECRYPTING WITH DISCOVERED KEY ===")
    for i, message in enumerate(encrypted_messages, 1):
        decrypted = decrypt_diana(message, discovered_key, diana_table)
        print(f"Message {i}: {decrypted}")
    
    print("\n=== INTERACTIVE MODE ===")
    print("Try different keys to decrypt the messages (enter 'q' to quit)")
    
    # Interactive mode to try different keys
    while True:
        key = input("\nEnter a key to try (or 'q' to quit): ").strip().upper()
        if key == 'Q':
            break
            
        for i, message in enumerate(encrypted_messages, 1):
            decrypted = decrypt_diana(message, key, diana_table)
            print(f"Message {i} decrypted with key '{key}':")
            print(decrypted)
            print()

if __name__ == "__main__":
    main()
