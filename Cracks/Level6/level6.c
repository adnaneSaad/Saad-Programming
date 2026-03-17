#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// This is the "Ghost" function. 
// No part of the main code calls this. You have to force it.
void secret_victory_room() {
    printf("\n--- CRITICAL SYSTEM ACCESS GRANTED ---\n");
    printf("SUCCESS: Level 6 Rooted! You manipulated the EIP/RIP.\n");
    exit(0);
}

void vuln_input() {
    char buffer[16]; // This is way too small...
    printf("Enter the override code: ");
    
    // The Vulnerability: gets() does not check for length!
    gets(buffer); 
    
    printf("You entered: %s\n", buffer);
}

int main() {
    printf("--- Level 6: The Stack Smasher ---\n");
    vuln_input();
    printf("NOPE: Standard execution finished. You failed to divert the flow.\n");
    return 0;
}
