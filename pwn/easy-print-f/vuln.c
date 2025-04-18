#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int win()
{

    printf("what how did you do it??????????");
    system("cat flag.txt");
}

int main()
{
    setbuf(stdout,NULL);
    setbuf(stdin,NULL);
    setbuf(stderr,NULL);
    char buffer[120];
    puts("Haha my buffer cant be overflowed and there is pie, ill even let you read and print twice");
    read(0, buffer, 120);
    printf(buffer);
    read(0, buffer, 120);
    printf(buffer);
    puts("nice try");

}
