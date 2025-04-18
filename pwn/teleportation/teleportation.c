#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void turn(char* actions[], u_int8_t state[], int* floor)
{
    switch(*floor) {
	case -88:
	    puts("You are in...some kind of dark cave? On the -88th floor?!\n");
	    break;
	case -1:
	    puts("You are in the basement on the -1st floor.\n");
	    break;
	case 0:
	    puts("You are in the main room on the 0th floor.\n");
	    break;
	case 1:
	    puts("You are in the living quarters on the 1st floor.\n");
	    break;
	case 2:
	    puts("You are in the arcane lab on the 2nd floor.\n");
	    break;
	case 3:
	    puts("You are in the library on the 3rd floor.\n");
	    break;
	case 4:
	    puts("You are on the balcony on the 4th floor.\n");
	    break;
	default:
	    puts("You are in...wait, where are you? How did you get here?\n");
	    break;
    }
    
    for(int i=0; i<4; i++) {
        printf("%d: %s\n", i, actions[i]);
    }

    u_int8_t input;
    scanf(" %c", &input);
    input -= 48;
    if(input > 3) {
        puts("That's not a valid action. Try again!\n");
        return;
    }

    switch(*floor) {
	case -88:
	    switch(input) {
		case 0:
		    puts("The cave is cramped and dark. You feel around until you find a yellow message stone.\n");
		    state[0] |= 1;
		    break;
		case 1:
		    if(state[0]) {
			char buf[50];
			puts("You touch the message stone, and glowing letters appear:\n");
			puts("\"Please leave an emergency message detailing your situation. You will be rescued soon.\"\n");
			fgetc(stdin);
			fgets(buf, 100, stdin);
		    } else {
			puts("You must look around the room first before interacting!\n");
		    }
		    break;
		case 2:
		    puts("There's no way up.\n");
		    break;
		case 3:
		    puts("There's no way down.\n");
		    break;
		default:
		    puts("That's not a valid action. Try again!\n");
		    break;
	    }
	    break;
	case -1:
	    switch(input) {
		case 0:
		    puts("The basement is filled with crates and old rolls of parchment. A purple wishing stone rests on top of a crate.\n");
		    state[1] |= 1;
		    break;
		case 1:
		    if(state[1] == 1){
			char buf[10];
			fgetc(stdin);
			puts("You touch the wishing stone, and glowing letters appear:\n");
			puts("\"What is your wish?\"\n");
			fgets(buf, 10, stdin);

			if(strcmp(buf, "runestone")) {
			    puts("Wish denied.\n");
			} else {
			    puts("Success! You now have a runestone.\n");
			    state[1] |= 2;
			}
		    } else if(state[1]) {
		        puts("You have already successfully made a wish!\n");
		    } else {
			puts("You must look around the room first before interacting!\n");
		    }
		    break;
		case 2:
		    puts("You take the staircase up to the 0th floor.\n");
		    *floor =  0;
		    break;
		case 3:
		    puts("You're already on the lowest floor.\n");
		    break;
		default:
		    puts("That's not a valid action. Try again!\n");
		    break;
	    }
	    break;
	case 0:
	    switch(input) {
		case 0:
		    puts("The main room is mostly empty, save for a kitchen with a stove and a pot.\n");
		    state[2] |= 1;
		    break;
		case 1:
		    if(state[2]) {
			puts("You taste the soup in the pot. It is cold and disgusting.\n");
		    } else {
			puts("You must look around the room first before interacting!\n");
		    }
		    break;
		case 2:
		    puts("You take the staircase up to the 1st floor.\n");
		    *floor =  1;
		    break;
		case 3:
		    puts("You take the staircase down to the -1st floor.\n");
		    *floor =  -1;
		    break;
		default:
		    puts("That's not a valid action. Try again!\n");
		    break;
	    }
	    break;
	case 1:
	    switch(input) {
		case 0:
		    puts("The living quarters contain several small bedrooms. One bed looks especially comfortable.\n");
		    state[3] |= 1;
		    break;
		case 1:
		    if(state[3]) {
			puts("You take a nap on the bed.\n");
		    } else {
			puts("You must look around the room first before interacting!\n");
		    }
		    break;
		case 2:
		    puts("You take the staircase up to the 2nd floor.\n");
		    *floor =  2;
		    break;
		case 3:
		    puts("You take the staircase down to the 0th floor.\n");
		    *floor =  0;
		    break;
		default:
		    puts("That's not a valid action. Try again!\n");
		    break;
	    }
	    break;
	case 2:
	    switch(input) {
		case 0:
		    puts("The arcane laboratory features various magical artifacts and tools. An elaborate arcane sigil on the floor has empty slots that should fit runestones.\n");
		    state[4] |= 1;
		    break;
		case 1:
		    if(state[4]) {
		        if(state[1] & 2) {
			    int buf[8];
			    int slot;
			    int num;

			    puts("Place your runestone into a slot [0-7].\n");
			    scanf("%d", &slot);

			    puts("The runestone glows and asks you to give it a number.\n");
			    scanf("%d", &num);

			    buf[slot] = num;
			    puts("I hope you cast the spell you wanted...\n");
			} else {
			    puts("You don't have anything that would fit in a slot.\n");
			}
		    } else {
			puts("You must look around the room first before interacting!\n");
		    }
		    break;
		case 2:
		    puts("You take the staircase up to the 3rd floor.\n");
		    *floor =  3;
		    break;
		case 3:
		    puts("You take the staircase down to the 1st floor.\n");
		    *floor =  1;
		    break;
		default:
		    puts("That's not a valid action. Try again!\n");
		    break;
	    }
	    break;
	case 3:
	    switch(input) {
		case 0:
		    puts("The library is filled with bookshelves and scroll racks. One book is sticking out of a bookcase.\n");
		    state[5] |= 1;
		    break;
		case 1:
		    if(state[5]) {
			puts("You pull on the book, and it falls out of the bookcase. Guess it wasn't a switch...\n");
		    } else {
			puts("You must look around the room first before interacting!\n");
		    }
		    break;
		case 2:
		    puts("You take the staircase up to the 4th floor.\n");
		    *floor = 4;
		    break;
		case 3:
		    puts("You take the staircase down to the 2nd floor.\n");
		    *floor =  2;
		    break;
		default:
		    puts("That's not a valid action. Try again!\n");
		    break;
	    }
	    break;
	case 4:
	    switch(input) {
		case 0:
		    puts("The balcony provides a view of the outside forest. In the middle, a large glowing crystal projects a beam of light upward into the sky.\n");
		    state[6] |= 1;
		    break;
		case 1:
		    if(state[6]) {
			puts("You touch the crystal. Your hand glows from the light. Nothing else happens.\n");
		    } else {
			puts("You must look around the room first before interacting!\n");
		    }
		    break;
		case 2:
		    puts("You're already on the highest floor.\n");
		    break;
		case 3:
		    puts("You take the staircase down to the 3rd floor.\n");
		    *floor = 3;
		    break;
		default:
		    puts("That's not a valid action. Try again!\n");
		    break;
	    }
	    break;
	default:
	    puts("You're stuck and you cannot take any actions. You will now be ejected from the tower as a failsafe.\n");
	    exit(-1);
    }
    return;
}

int main(int argc, char* argv[])
{
    setbuf(stdout,NULL);
    setbuf(stdin,NULL);
    setbuf(stderr,NULL);

    int floor = 0;

    char* actions[4];
    actions[0] = "Look around";
    actions[1] = "Interact";
    actions[2] = "Go up";
    actions[3] = "Go down";

    u_int8_t state[7];
    for(int i=0; i<7; i++) {
        state[i] = 0;
    }

    puts("You have entered a mysterious tower...\n");
    while(1) {
        turn(actions, state, &floor);
    }

    return 0;
}
