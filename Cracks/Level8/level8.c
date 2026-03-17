#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct user_session {
    char buffer[16];
    int authenticated;
};

int main() {
    struct user_session *session = malloc(sizeof(struct user_session));
    session->authenticated = 0;
    printf("--- Level 8: Heap Overwrite ---\n");
    printf("Current Auth Status: %d\n", session->authenticated);
    printf("Enter Admin Key: ");
    gets(session->buffer); 
    if (session->authenticated != 0) {
        printf("\n[SUCCESS] Gatekeeper bypassed! Status: %d\n", session->authenticated);
        printf("Flag: {H3AP_FL0W_D4T4_0V3RWR1T3}\n");
    } else {
        printf("\n[FAILED] Gatekeeper says NO.\n");
    }
    free(session);
    return 0;
}
