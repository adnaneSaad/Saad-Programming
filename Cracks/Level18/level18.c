#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void victory() {
    printf("\n--- LEVEL 18: CLEAR ---\n");
    printf("Flag: 3nv_v4r14bl3_m4st3r\n");
}

int main() {
    char *env_pass = getenv("GHOST_KEY");
    char input[64];

    printf("--- LEVEL 18: THE GHOST ---\n");

    if (env_pass == NULL) {
        printf("[!] ERROR: The Ghost is missing. Set GHOST_KEY to continue.\n");
        return 1;
    }

    printf("Enter the passkey: ");
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = 0;

        if (strcmp(input, env_pass) == 0) {
            victory();
        } else {
            printf("The Ghost remains silent. Wrong key.\n");
        }
    }

    return 0;
}
