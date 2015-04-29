level01 
This is a very simple one. Let us have a look at how it goes. Run the binary in gdb Disassemble the given binary.
disas main 
Notice the compare statement 
0x0804808f <+15>:    cmp $0x10f,%eax 
0x08048094 <+20>: je 0x80480dc <YouWin>
-Check out the decimal value for 0x10f, which is 271. Knowing this value gives you the shell!

level02 
In level 02, have a look at the code. 
Goal: Invoke the catcher function somehow to get the shell. Catcher is handle function of SIGFPE signal. 
Technique: Read the manual page of SIGFPE. You will find that it gets invoked during errors in arithmetic operations, like division by zero.
As per code, we can’t perform division by zero. Dividing integer minimum (or lesser number) by -1
would call SIGFPE. Why waiting? Go ahead and get the shell!

