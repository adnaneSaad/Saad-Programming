#include <stdio.h>
#include <stdlib.h>

int target_variable = 0; // The goal is to change this to 1337

void give_flag() {
    printf("\n[SUCCESS] Memory Modified! Here is your flag: {W34P0N1Z3D_PR1NTF_2026}\n");
}

int main() {
    char user_input[100];

    printf("--- Level 10: The God Mode Write ---\n");
    printf("Target Variable Address: %p\n", &target_variable);
    printf("Target Variable Current Value: %d\n", target_variable);
    
    printf("Enter your payload: ");
    fgets(user_input, sizeof(user_input), stdin);

    // The vulnerability returns...
    printf(user_input);

    if (target_variable == 1337) {
        give_flag();
    } else {
        printf("\nTarget is still %d. Try harder!\n", target_variable);
    }

    return 0;
}
