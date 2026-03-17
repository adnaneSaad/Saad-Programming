#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <string.h>
#include <unistd.h>

void victory() {
    printf("--- LEVEL 15: CLEAR ---\n");
    printf("Flag: 4nt1_d3bu6_m4st3r\n");
}

int main(int argc, char *argv[]) {
    char input[32];
    
    // THE WATCHDOG: This checks if a debugger is attached
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0) {
        printf("!!! DEBUGGER DETECTED !!!\n");
        printf("The Watchdog has bitten you. Exit.\n");
        exit(1);
    }

    printf("--- LEVEL 15: THE WATCHDOG ---\n");
    printf("Enter the passkey: ");
    
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = 0;
        
        // A simple check, but you can't see it if you can't trace it!
        if (strcmp(input, "9921") == 0) {
            victory();
        } else {
            printf("Wrong. The Watchdog is unimpressed.\n");
        }
    }

    return 0;
}
