###Heap0

In the source code, we can see that the function pointer is pointing to address of no-winner. 
We have a strcpy() which can overwrite the address of function pointer with address of winner. 

###Heap1

There are two arguments here and two strcpy(). The first strcpy() could be used 
to overwrite the pointer to the value in first argument. The heap looks somewhat like 
this after both the strcpy is done:

```
0x804a000:      0x00000000      0x00000011      0x00000001      0x0804a018
0x804a010:      0x00000000      0x00000011      0x41414141      0x00000000
0x804a020:      0x00000000      0x00000011      0x00000002      0x0804a038
0x804a030:      0x00000000      0x00000011      0x42424242      0x00000000
0x804a040:      0x00000000      0x00020fc1      0x00000000      0x00000000
```
