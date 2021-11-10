#include <stdio.h>

void overflow() {
    char buffer[64];

    printf("try your best\n");
    gets(buffer);
}

int main() {
    overflow();
}
