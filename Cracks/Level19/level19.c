#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

// This is the "Encrypted" logic for: return (strcmp(a, b) == 0);
unsigned char encrypted_logic[] = { 0x55, 0x48, 0x89, 0xe5, 0x48, 0x83, 0xec, 0x10, 0x48, 0x89, 0x7d, 0xf8, 0x48, 0x89, 0x75, 0xf0, 0x48, 0x8b, 0x55, 0xf8, 0x48, 0x8b, 0x45, 0xf0, 0x48, 0x89, 0xd7, 0x48, 0x89, 0xc6, 0xe8, 0x00, 0x00, 0x00, 0x00, 0x85, 0xc0, 0x0f, 0x94, 0xc0, 0x0f, 0xb6, 0xc0, 0xc9, 0xc3 };

typedef int (*check_func)(const char*, const char*);

int main() {
    char input[64];
    const char *key = "poly_99";
    
    // Allocate executable memory for our "Ghost Code"
    void *mem = mmap(NULL, sizeof(encrypted_logic), PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
    
    // Decrypt (XOR) the logic into the executable memory
    for(int i = 0; i < sizeof(encrypted_logic); i++) {
        ((unsigned char*)mem)[i] = encrypted_logic[i] ^ 0x00; // In a real polymorph, this would be a real key
    }

    check_func is_valid = (check_func)mem;

    printf("--- LEVEL 19: THE POLYMORPH ---\n");
    printf("Enter the passkey: ");
    
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = 0;

        if (is_valid(input, key)) {
            printf("\n--- LEVEL 19: CLEAR ---\nFlag: m3m0ry_unp4ck_5uccess\n");
        } else {
            printf("The code is masked. Wrong key.\n");
        }
    }

    return 0;
}
