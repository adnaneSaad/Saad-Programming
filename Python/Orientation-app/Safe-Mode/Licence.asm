section .text
    global verify_logic

verify_logic:
    ; Python will pass the input address in RDI
    ; The secret "Saad-2012" XORed with 0x42
    mov rsi, secret_data 
    mov rcx, 0

.loop:
    mov al, [rdi + rcx]    ; Get user input char
    xor al, 0x42           ; XOR it
    cmp al, [rsi + rcx]    ; Compare with secret
    jne .fail
    inc rcx
    cmp rcx, 9
    jne .loop

    mov rax, 0             ; Success!
    ret

.fail:
    mov rax, 1             ; Fail!
    ret

section .data
    secret_data db 0x70, 0x73, 0x71, 0x61, 0x0f, 0x72, 0x70, 0x71, 0x73
