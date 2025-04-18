#include <stdlib.h>
#include <stdio.h>
#include <windows.h>

int main() {
    // Viola: C C C B C D G G F E
    const char* hint = "T3JnYW5pYw==";
    const char* string = "Q0NDQkNER0dGRQ==";
    char notes[10];
    notes[0] = 'P';
    notes[1] = 'P';
    notes[2] = 'P';
    notes[3] = 'O';
    notes[4] = 'P';
    notes[5] = 'Q';
    notes[6] = 'T';
    notes[7] = 'T';
    notes[8] = 'S';
    notes[9] = 'R';

    while(1) {
        for(int i=0; i<10; i++) {
            Sleep(1000);
            printf("Note: %c\n", notes[i]-13);
        }
    }

    return 0;
}