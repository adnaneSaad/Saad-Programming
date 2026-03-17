#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// A simple XOR key to hide the real password
#define SECRET_XOR 0x42 

void victory() {
    printf("--- LEVEL 16: CLEAR ---\n");
    printf("Flag: x0r_is_n0t_3n0u6h\n");
}

int main() {
    char input[64];
    // The "obfuscated" version of the password "6789"
    // Each char is XORed with 0x42
    int target[] = {54 ^ 0x42, 55 ^ 0x42, 56 ^ 0x42, 57 ^ 0x42}; 
    
    printf("--- LEVEL 16: THE OBFUSCATOR ---\n");
    printf("Enter the passkey: ");
    
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = 0; // Remove newline

        int match = 1;
        for (int i = 0; i < 4; i++) {
            if ((input[i] ^ SECRET_XOR) != target[i]) {
                match = 0;
                break;
            }
        }

        if (match && strlen(input) == 4) {
            victory();
        } else {
            printf("Wrong. Your logic is clouded.\n");
        }
    }
    
    return 0;
}
