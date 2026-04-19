#include <stdio.h>
#include <string.h>

// The "X-Final" was too easy, so now we hide it.
// This is "Secret21" XORed with 0x42
unsigned char hidden_key[] = {0x11, 0x27, 0x21, 0x30, 0x27, 0x36, 0x70, 0x73}; 

int main() {
    char input[64];
    char decrypted[9];
    
    printf("--- LEVEL 21: THE ENCRYPTED GATE ---\n");
    printf("Enter Authorization Code: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0; // Remove newline

    // Decrypt the key in memory only when checking
    for(int i = 0; i < 8; i++) {
        decrypted[i] = hidden_key[i] ^ 0x42;
    }
    decrypted[8] = '\0';

    if (strcmp(input, decrypted) == 0) {
        printf("[+] Access Granted. Victory!\n");
    } else {
        printf("[!] Access Denied. Sequence incorrect.\n");
    }

    return 0;
}
