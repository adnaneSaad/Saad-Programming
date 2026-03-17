#include <stdio.h>
#include <string.h>

int main() {
    char input[100];
    int secret = 0x31337; // Level 3 uses a bigger hex number
    char password[100];
    
    // Level 3 logic: The password is "fedorian_" + the hex value
    sprintf(password, "fedorian_%d", secret); 

    printf("Enter Level 3 Key: ");
    scanf("%99s", input);

    if (strcmp(input, password) == 0) {
        printf("SUCCESS! Level 3 Cleared.\n");
    } else {
        printf("NOPE. Try again.\n");
    }
    return 0;
}
