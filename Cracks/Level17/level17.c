#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

void victory() {
    printf("\n--- LEVEL 17: CLEAR ---\n");
    printf("Flag: t1m3_wa1ts_f0r_n0_0n3\n");
}

long long get_micros() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (tv.tv_sec * 1000000LL) + tv.tv_usec;
}

int main() {
    char input[10];
    const char* secret = "4242";
    long long start, end;

    printf("--- LEVEL 17: THE TIME BOMB ---\n");
    printf("Enter the 4-digit passkey: ");
    fflush(stdout);

    start = get_micros();
    if (fgets(input, sizeof(input), stdin)) {
        end = get_micros();
        input[strcspn(input, "\n")] = 0;

        // The "Explosion" Check: 50,000 micros = 50ms
        if ((end - start) > 50000) {
            printf("\n[!] BOOM! Too slow. The Watchdog timed you out.\n");
            return 1;
        }

        if (strcmp(input, secret) == 0) {
            victory();
        } else {
            printf("Wrong key. Logic intact.\n");
        }
    }

    return 0;
}
