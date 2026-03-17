#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    // This is the "Hardcoded String"
    char password[] = "fedora_rocks_2026"; 

    printf("--- LEVEL 1 CRACKME ---\n");
    printf("Enter the secret password: ");
    
    // Get user input
    scanf("%63s", input);

    // The logic we want to reverse
    if (strcmp(input, password) == 0) {
        printf("\n[+] SUCCESS! Access Granted.\n");
    } else {
        printf("\n[-] ERROR: Access Denied.\n");
    }

    return 0;
}
