#include <stdio.h>
#include <string.h>

int main() {
    char input[10];
    // The "Scrambled" secret: Not readable in the 'Strings' window!
    unsigned char secret[] = { 0x1d, 0x17, 0x01, 0x0c, 0x1e, 0x0b, 0x5a }; 
    unsigned char key = 0x56; // The "Magic Number"
    
    printf("Enter Level 23 Key: ");
    fgets(input, 10, stdin);
    input[strcspn(input, "\n")] = 0;

    for (int i = 0; i < 7; i++) {
        // The XOR Transformation: Beautiful, reversible, and sneaky.
        if ((input[i] ^ key) != secret[i]) {
            puts("Access Denied.");
            return 1;
        }
    }

    puts("Victory! You've mastered the XOR Veil.");
    return 0;
}
