#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char secret_flag[] = "{F0RM4T_STR1NG_L34K_2026}";
    char user_input[100];

    printf("--- Level 9: The Memory Mirror ---\n");
    printf("Tell me something, and I will repeat it: ");
    
    // Using fgets is "safe" from overflows...
    fgets(user_input, sizeof(user_input), stdin);

    // BUT this is the fatal mistake:
    // It should be printf("%s", user_input);
    printf(user_input); 

    printf("\n--- Task Complete ---\n");
    return 0;
}
