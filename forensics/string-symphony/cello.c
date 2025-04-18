#include <stdlib.h>
#include <stdio.h>
#include <windows.h>

int main() {
    // Cello: C E F G A F G G G C 
    const char* hint = "U2NvcmVz";
    const char* string = "Q0VGR0FGR0dHQw==";
    char notes[10];
    notes[0] = 'P';
    notes[1] = 'R';
    notes[2] = 'S';
    notes[3] = 'T';
    notes[4] = 'N';
    notes[5] = 'S';
    notes[6] = 'T';
    notes[7] = 'T';
    notes[8] = 'T';
    notes[9] = 'P';

    while(1) {
        for(int i=0; i<10; i++) {
            Sleep(1000);
            printf("Note: %c\n", notes[i]-13);
        }
    }

    return 0;
}