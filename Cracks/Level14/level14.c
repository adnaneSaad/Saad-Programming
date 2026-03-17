#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

// The Final Boss Payload: x86_64 shellcode XORed with a secret key.
// This is the polymorphic code that changes based on your input key.
unsigned char final_boss_code[] = {
    0x3f, 0x77, 0x11, 0x01, 0x01, 0x01, 0x01, 0x3f, 0x77, 0x71, 
    0x31, 0x01, 0x01, 0x01, 0x01, 0x3f, 0x77, 0x76, 0x31, 0x01, 
    0x01, 0x01, 0x01, 0x3f, 0x77, 0x72, 0x11, 0x0a, 0x01, 0x01, 
    0x01, 0x3f, 0x77, 0x31, 0xd2, 0x48, 0x8d, 0x35, 0x07, 0x00, 
    0x00, 0x00, 0x0f, 0x05, 0xc3,
    // Secret Flag Data
    0x1a, 0x1c, 0x1a, 0x1a, 0x1c, 0x0c, 0x0c, 0x0a
};

void run_mimic(int key) {
    long pagesize = sysconf(_SC_PAGESIZE);
    
    // Allocate memory with a "No-Execute" initial state for security
    void *mem = mmap(NULL, pagesize, PROT_READ | PROT_WRITE, 
                     MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
    
    if (mem == MAP_FAILED) {
        perror("mmap");
        return;
    }

    // Decrypt the Mimic payload into the allocated memory
    for (int i = 0; i < sizeof(final_boss_code); i++) {
        ((unsigned char*)mem)[i] = final_boss_code[i] ^ key;
    }

    // Flip memory to Read/Execute. Fedora 43 monitors this transition.
    if (mprotect(mem, pagesize, PROT_READ | PROT_EXEC) == -1) {
        perror("mprotect");
        munmap(mem, pagesize);
        return;
    }

    // Define the function pointer as volatile to force execution
    void (*volatile boss_func)() = (void (*)())mem;

    printf("[*] Jumping to Mimic payload at %p...\n", mem);
    
    // THE JUMP: If the key is wrong, this triggers SIGILL or SIGSEGV
    boss_func(); 

    printf("[*] Payload returned successfully.\n");

    // Clean up memory
    munmap(mem, pagesize);
}

int main() {
    int key;
    printf("--- LEVEL 14: THE MIMIC ---\n");
    printf("Enter Final Key: ");
    
    // Read the user input key
    if (scanf("%d", &key) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    run_mimic(key);
    return 0;
}
