#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
    char password[8]; // For length 7 + null terminator
    char command[128];
    char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    int charset_len = strlen(charset);

    printf("🚀 Starting C-Smasher on /dev/shm/level23...\n");

    // This is a simplified nested loop for length 3 
    // (You'd use recursion or more loops for length 7)
    for (int i = 0; i < charset_len; i++) {
        for (int j = 0; j < charset_len; j++) {
            for (int k = 0; k < charset_len; k++) {
                
                sprintf(password, "%c%c%c", charset[i], charset[j], charset[k]);
                
                // Construct the command to pipe the password
                // We use /dev/shm/ to keep it in RAM
                sprintf(command, "echo %s | /dev/shm/level23 > /dev/null 2>&1", password);
                
                int status = system(command);

                if (status == 0) { // Assuming 0 means "Success"
                    printf("\n🏆 FOUND IT: %s\n", password);
                    return 0;
                }
            }
        }
    }
    return 0;
}
