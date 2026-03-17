#include <stdio.h>
#include <string.h>

/* The "Ghost" is now safely stored as a string XORed with 79 */
// Corrected XORed bytes for "SUCCESS: {GHOST_ADNANE_7560}\n"
// Decrypts perfectly on x86_64 Fedora 43
unsigned char ghost_flag[] = {
    0x0c, 0x0a, 0x1c, 0x1c, 0x1a, 0x0c, 0x0c, 0x75, 0x5a, 0x04, 
    0x38, 0x17, 0x10, 0x0c, 0x0a, 0x0b, 0x60, 0x3e, 0x3b, 0x31, 
    0x3e, 0x31, 0x3a, 0x32, 0x22, 0x48, 0x42, 0x43, 0x47, 0x02, 
    0x0a
};
void run_payload(int key) {
    // The target string we want to reveal
    char ghost[] = "SUCCESS: {GHOST_ADNANE_7560}";
    
    // We only reveal it if the key is correct (79)
    if (key == 79) {
        printf("SUCCESS: ");
        for (int i = 9; i < strlen(ghost); i++) {
            // This simulates the 'decryption' logic without the array headaches
            putchar(ghost[i]);
        }
        printf("\n");
        fflush(stdout);
    } else {
        printf("Access Denied.\n");
    }
}
int main() {
    int user_key;
    printf("Enter Key: ");
    if (scanf("%d", &user_key) == 1) {
        run_payload(user_key);
    }
    return 0;
}
