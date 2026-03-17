#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void victory() {
    printf("\n[!!!] SYSTEM BYPASSED: Canary didn't stop you!\n");
    printf("Flag: {C4N4RY_1S_D34D}\n");
    exit(0);
}

void vuln() {
    char buffer[32];
    printf("--- Level 7: The Canary Challenge ---\n");
    
    // FIRST FLAW: A Format String Vulnerability (to leak the canary)
    printf("Identify yourself: ");
    fgets(buffer, 32, stdin);
    printf("Hello, ");
    printf(buffer); // <--- DANGEROUS: No format specifier!

    // SECOND FLAW: The usual Buffer Overflow
    printf("\nEnter override command: ");
    gets(buffer); // <--- Still using gets(), but the canary is watching.
}

int main() {
    vuln();
    printf("Standard exit. You failed to bypass the bird.\n");
    return 0;
}
