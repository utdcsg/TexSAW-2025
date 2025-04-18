#include <stdio.h>
#include <string.h>

void check_password(char *input) {
    unsigned char key[] = {0xcb, 0x95, 0xd1,0xfa,0xd1,0xcd,0x96,0xfa,0xc3,0xc9,0x91,0xc2}; 
    int len = strlen(input);
   
    for (int i = 0; i < 12; i++) {
        if ((input[i] ^ 0xA5) != key[i]) {
            printf("Wrong password!\n");
            return;
        }
    }

    printf("Correct! Here's your flag: texsaw{%s}\n", input);
}

int main() {
    char input[32];
    printf("Enter password: ");
    scanf("%31s", input);
    check_password(input);
    return 0;
}

