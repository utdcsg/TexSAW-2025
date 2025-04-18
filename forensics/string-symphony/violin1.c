#include <stdlib.h>
#include <stdio.h>
#include <windows.h>

int main() {
    // Violin 1: E C F D E F E D D C
    const char* hint = "REGISTRY_HKLM";
    const char* string = "RUNGREVGRUREQw==";
    char notes[10];
    notes[0] = 'R';
    notes[1] = 'P';
    notes[2] = 'S';
    notes[3] = 'Q';
    notes[4] = 'R';
    notes[5] = 'S';
    notes[6] = 'R';
    notes[7] = 'Q';
    notes[8] = 'Q';
    notes[9] = 'P';

    while(1) {
        for(int i=0; i<10; i++) {
            Sleep(1000);
            printf("Note: %c\n", notes[i]-13);
        }
    }

    return 0;
}