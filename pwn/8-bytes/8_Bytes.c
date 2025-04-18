#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include<unistd.h>

void print_flag() {
    system("cat flag.txt");
}

void vuln() {
	char buffer[8];
    unsigned char secret[8] = {0x12,0x34,0x56,0x78,0x12,0x34,56};
    long val;

	printf("Enter your input: ");
	read(0, buffer, 24);

    memcpy(&val, secret, sizeof(long));
	if (val == 0x2148534f4f4f4857) {
		print_flag();
	} else {
		printf("Try again! Secret = 0x%016llx, needed 0x2148534f4f4f4857\n", val);
	}
}

int main() {
	//setbuf(stdout, NULL);
	vuln();
	return 0;
}
