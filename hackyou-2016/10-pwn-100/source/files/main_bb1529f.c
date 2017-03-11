#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    struct a {
        char buffer[256];
        int set_me;
    } _a;

    _a.set_me = 0xcafebabe;

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    printf("Value: 0x%08x\n", _a.set_me);
    gets(_a.buffer);

    printf("You input %u bytes.\n", strlen(_a.buffer));
    printf("Value: 0x%08x\n", _a.set_me);

    if (_a.set_me == 0xdeadbeef) {
        printf("Take your flag...\n");
        system("cat flag.txt");
    }

    return 0;
}
