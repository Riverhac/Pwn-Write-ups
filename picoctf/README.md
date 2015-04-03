Format: We can pop the elements of the stack using this vulnerability. 

Goal: Replace the value of secret with 1337 to get shell 

Method: Find address of secret. Global variable and hence in .data section. Run objdump -d

Try to find if you can find the address of secret in the stack by poping its content using %p as arguments to format. 

You find that the 7th argument is the address of secret. Replace it as shown in the exploit ! :)
