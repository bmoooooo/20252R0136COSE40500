#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x;

    printf("Before write: x = %d\n", x);

    int y = *ptr;  // simulate copy
    y = 20;

    printf("After write:\n");
    printf("x = %d\n", x);
    printf("y = %d\n", y);

    return 0;
}
