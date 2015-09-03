###Heap0

In the source code, we can see that the function pointer is pointing to address of `no_winner()`. 
We have a `strcpy()` which can overwrite the address of function pointer with address of `winner()`.
This is a basic exploit where we have to find the address of `winner()`, the offset, and make 
a proper payload to be passed as the argument. 

###Heap1

There are two arguments here and two strcpy(). The first strcpy() could be used 
to overwrite the pointer to the value in first argument. The heap looks somewhat like 
this after both the strcpy is done:

After opening the binary in gdb, run it with random arguments.

`$ r AAAA BBBB`

```
0x804a000:      0x00000000      0x00000011      0x00000001      0x0804a018

0x804a010:      0x00000000      0x00000011      0x41414141      0x00000000

0x804a020:      0x00000000      0x00000011      0x00000002      0x0804a038

0x804a030:      0x00000000      0x00000011      0x42424242      0x00000000

0x804a040:      0x00000000      0x00020fc1      0x00000000      0x00000000
```

Notice that there is a pointer in the heap that points to the location 
where the value is getting copied. `0x0804a018` is exactly the address 
where we can see `0x41414141`. Similarly, `0x0804a038` is the place where 
`0x42424242` got written. 

We can exploit this by overflowing the first argument we pass and overwriting 
the pointer to the second argument. If we could rewrite it to the address 
of `GOT("puts")` [printf appears as puts in GOT table], then what we enter to arg2 
will be the new value of puts as the function pointer is changed. 
The next step is simple. Pass the second argument as the address of `winner()`.
