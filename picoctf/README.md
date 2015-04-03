<b>Format</b>

Goal: Replace the value of secret with 1337 to get shell 

Method: Find address of secret. It is a global variable and hence found in .data section. 
Run objdump -d
Try to find if you can find the address of secret in the stack by poping its content using %p as arguments to format.
./format "python -c 'print "%p."*10'"
You find that the 7th argument is the address of secret. Replace it as shown in the exploit ! :)
