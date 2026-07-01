#include <stdio.h>

int main() {
    printf("Hello from ARM! Running natively on my Dell Precision via QEMU.\n");
    #ifdef __arm__
        printf("Architecture: 32-bit ARM detected.\n");
    #endif
    return 0;
}
