#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    // This is the "Hash" we are looking for
    int secret_key[] = {110, 101, 100, 111, 114, 105, 97, 110}; 
    int success = 1;

    printf("--- Level 5: The Iterator ---\n");
    printf("Enter the secret string: ");
    scanf("%63s", input);

    if (strlen(input) != 8) {
        printf("NOPE: Wrong length!\n");
        return 1;
    }

    // The Loop: This is what creates the 'jg' or 'jl' in assembly
    for (int i = 0; i < 8; i++) {
        if ((int)input[i] != secret_key[i]) {
            success = 0;
            break;
        }
    }

    if (success) {
        printf("SUCCESS: Level 5 Cleared! You're a natural.\n");
    } else {
        printf("NOPE: That's not it.\n");
    }

    return 0;
}
