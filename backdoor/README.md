Echo:

Here is the link to the challenge: https://backdoor.sdslabs.co/challenges/ECHO

Disassemble the code, you find a function called sample, which is never called. You can also see that it is
reading from a file called flag.txt. 

Goal: Overwrite the return address from test to the address of sample. 

Method: Find the address of sample using objdump -d --> (0x804854d). 
We need to find the offset. Refer to the comments in exploit for
that. Find the exact padding and then pass the address packed. 

