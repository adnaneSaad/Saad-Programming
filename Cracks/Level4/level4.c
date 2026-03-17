#include <stdio.h>
#include <string.h>

int main() {
    int secret = 0x539; // 1337 in decimal
    int user_input;
    
    printf("Enter Level 4 Key: ");
    if (scanf("%d", &user_input) != 1) {
        printf("Invalid input!\n");
        return 1;
    }

    // A simple math check instead of a string check
    if ((user_input ^ 0xABC) == secret) {
        printf("SUCCESS: Level 4 Cleared.\n");
    } else {
        printf("NOPE. Try again.\n");
    }
    return 0;
}
