#include <stdio.h>
#include <string.h>

int verify_password(char *input) {

    // Obfuscated password
    unsigned char obfuscated[] = {0x1f, 0x43, 0x31, 0x3a, 0x16, 0x40, 0x10, 0x17, 
                                 0x20, 0x11, 0x3a, 0x15, 0x47, 0x16, 0x24, 0x30, 
                                 0x17, 0x07, 0x17};
    
    
    // 1f 43 31 3a 16 40 10 17 20 11 3a 15 47 16 24 30 17 07 17 (hash pass)
    
       
    // 71 73 65 65 65 73 73 65 65 65 65 65 73 65 77 47 78 75 73 (key)
    
   
    // 6e 30 54 5f 73 33 63 72 45 74 5f 70 34 73 53 77 6f 72 64 (actual one)
    
    
    // XOR key
    unsigned char key[] = {0x71, 0x73, 0x65, 0x65, 0x65, 0x73, 0x73, 0x65, 
                          0x65, 0x65, 0x65, 0x65, 0x73, 0x63, 0x77, 0x47, 
                          0x78, 0x75, 0x73};
    
    unsigned char temp;
    int i;
    int password_len = sizeof(obfuscated);
    
    
    // Check input length first
    if (strlen(input) != password_len - 1) {
        return 0;
    }
    
    // XOR decoding
    for (i = 0; i < password_len - 1; i++) {
        temp = obfuscated[i] ^ key[i];
        if (input[i] != temp) {
            return 0;
        }
    }
    
    return 1;
}

int main() {
    char user_input[50];
    char password[14] = "ha_you_thought";
    
    printf("Enter the secret password: ");
    scanf("%49s", user_input);
    
    if (verify_password(user_input)) {
        printf("Correct! The flag is: texsaw{%s}\n", user_input);
    } else {
        printf("Incorrect password! Try again.\n");
    }
    
    return 0;
}