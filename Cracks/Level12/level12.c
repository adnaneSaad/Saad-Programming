#include <stdio.h>
#include <sys/ptrace.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

void check_spy() {
    // If ptrace fails, it means a debugger (Cutter) is already attached!
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0) {
        printf("[!] SPY DETECTED! Deploying Fake Flag...\n");
        printf("Flag: {NOT_THE_REAL_ONE_NICE_TRY}\n");
        exit(1);
    }
}

int main() {
    check_spy();
    
    char pass[16];
    printf("Enter Access Code: ");
    scanf("%15s", pass);

    if (strcmp(pass, "Saad_79_2026") == 0) {
        printf("SUCCESS: {ANTI_DEBUG_BYPASS_MASTER}\n");
    } else {
        printf("ACCESS DENIED.\n");
    }
    return 0;
}
