#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

void victory() {
    printf("\n[!!!] LEVEL 20: COMPLETE [!!!]\n");
    printf("FINAL FLAG: k3rn3l_lvl_h4ck3r_42\n");
    printf("Congratulations, Saad! You've cleared the gauntlet.\n");
}

int main() {
    printf("--- LEVEL 20: THE KERNEL GATE ---\n");
    printf("[*] Checking for System Authorization... ");
    fflush(stdout);

    // This is the Gate. It checks for a hidden file in /tmp
    if (access("/tmp/.gate_authorized", F_OK) == -1) {
        printf("\n[!] ERROR: Authorization file missing in /tmp.\n");
        return 1;
    }

    printf("FOUND.\n[+] Enter the Final Sequence: ");
    char sequence[16];
    if (fgets(sequence, sizeof(sequence), stdin)) {
        sequence[strcspn(sequence, "\n")] = 0;

        // The secret trigger is 'X-Final'
        if (strcmp(sequence, "X-Final") == 0) {
            victory();
        } else {
            printf("[!] Access Denied. Sequence incorrect.\n");
        }
    }

    return 0;
}
