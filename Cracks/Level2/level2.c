#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    int secret_num = 0x1337 * 2; // The CPU does this math live
    char key[16];
    sprintf(key, "fedorian_%d", secret_num); 

    printf("--- LEVEL 2 CRACKME ---\n");
    printf("Enter the dynamic key: ");
    scanf("%63s", input);

    if (strcmp(input, key) == 0) {
        printf("[+] SUCCESS! Level 2 Cleared.\n");
    } else {
        printf("[-] ERROR: Wrong key.\n");
    }
    return 0;
}
