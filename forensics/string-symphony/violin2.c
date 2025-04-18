#include <stdlib.h>
#include <stdio.h>
#include <windows.h>

int main() {
    // Violin 2: G G A G A A C B B C
    const char* hint = "U09GVFdBUkU=";
    const char* string = "R0dBR0FBQ0JCQw==";
    char notes[10];
    notes[0] = 'T';
    notes[1] = 'T';
    notes[2] = 'N';
    notes[3] = 'T';
    notes[4] = 'N';
    notes[5] = 'N';
    notes[6] = 'P';
    notes[7] = 'O';
    notes[8] = 'O';
    notes[9] = 'P';

    while(1) {
        for(int i=0; i<10; i++) {
            Sleep(1000);
            printf("Note: %c\n", notes[i]-13);
        }
    }

    return 0;
}