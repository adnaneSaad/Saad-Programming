#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    // The obfuscated key
    int key[] = {154, 184, 184, 190, 180, 100, 100, 114, 192, 114, 114, 190};
    
    printf("Enter Access Code: ");
    scanf("%s", input);

    if (strlen(input) != 12) {
        printf("ACCESS DENIED.\n");
        return 1;
    }

    for (int i = 0; i < 12; i++) {
        // The Math Gate: (input[i] * 2) - 10
        if ((input[i] * 2) - 10 != key[i]) {
            printf("ACCESS DENIED.\n");
            return 1;
        }
    }

    printf("SUCCESS: {LOGIC_GATE_OPEN_2026}\n");
    return 0;
}
