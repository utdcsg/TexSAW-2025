.intel_syntax noprefix
.global main

main:
    push   rbp
    mov    rbp,rsp
    lea    rcx,[rbp-0x20]
    mov    rax,0x0
    mov    rdi,0x0
    mov    rsi,rcx
    mov    rdx,0x80
    syscall
    pop    rbp
    ret

weird_func:
    push   rbp
    mov    rbp,rsp
    pop    rdi
    pop    rbp
    ret

