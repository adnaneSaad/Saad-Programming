#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("--- LEVEL 22: THE LOGIC GATE ---\n");
    printf("Enter Access Code: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;

    // The "Length" Check: Password MUST be 7 characters
    if (strlen(input) != 7) {
        goto fail;
    }

    // Character-by-Character Logic:
    // This prevents you from finding "Secret22" in one piece.
    if (input[0] != 'K') goto fail;          // First char is 'K'
    if (input[1] != (input[0] + 4)) goto fail; // 'K' + 4 = 'O'
    if (input[2] != 'R') goto fail;
    if (input[3] != 'N') goto fail;
    if (input[4] != (0x45)) goto fail;       // Hex for 'E'
    if (input[5] != 'L') goto fail;
    if (input[6] != '!') goto fail;

    printf("[+] Access Granted. Level 22 Clear!\n");
    return 0;

fail:
    printf("[!] Access Denied.\n");
    return 1;
}
