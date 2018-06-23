# Skipping Rope
Pwn

## Challenge 
> How high and how fast can you go on the skipping rope?

> nc ctf.pwn.sg 1501

> Creator - amon (@nn_amon)

## Solution

Hopper

	int skipping_rope() {
	    var_8 = mmap(0x0, 0x2000, 0x7, 0x22, 0xffffffff, 0x0);
	    // mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);

	    for (var_C = 0x0; var_C <= 0xff; var_C = var_C + 0x1) {
	            rax = read(0x0, var_8 + sign_extend_64(var_C << 0x4), 0x6);
	            // rax = read(0x0, var_8 + var_C * 16, 0x6);
	            // rax = read(stdin, var_8[16 * var_C], 6 /* bytes */);
	    }
	    rax = 0x0;
	    rax = (var_8)();
	    return rax;
	}

Checksec

	../checksec.sh/checksec -f ./skippingrope 
	RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	FORTIFY	Fortified Fortifiable  FILE
	Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   No	0		2	./skippingrope

https://github.com/ctfs/write-ups-2013/tree/master/pico-ctf-2013/rop-2
http://crowell.github.io/blog/2014/11/23/pwning-with-radare2/
https://seshagiriprabhu.wordpress.com/2014/10/26/return-to-libc-attack/
https://github.com/ctfs/write-ups-2013/tree/master/pico-ctf-2013/overflow-5
https://zolmeister.com/2013/05/rop-return-oriented-programming-basics.html
http://willcodeforfoo.com/2012/02/capture-the-flag
http://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html
https://pwning.re/2016/11/22/qiwi-ctf-writeup/

	# gdb skippingrope 
	(gdb) r
	Starting program: /FILES/cctf/skippingrope 
	^C
	Program received signal SIGINT, Interrupt.
	0x00007ffff7b15700 in __read_nocancel ()
	    at ../sysdeps/unix/syscall-template.S:84
	84	../sysdeps/unix/syscall-template.S: No such file or directory.
	(gdb) info sharedlibrary
	From                To                  Syms Read   Shared Object Library
	0x00007ffff7dd9aa0  0x00007ffff7df5340  Yes         /lib64/ld-linux-x86-64.so.2
	0x00007ffff7a59910  0x00007ffff7b83403  Yes         /lib/x86_64-linux-gnu/libc.so.6

	(gdb) r
	Starting program: /FILES/cctf/skippingrope 
	^C
	Program received signal SIGINT, Interrupt.
	0x00007ffff7b15700 in __read_nocancel () at ../sysdeps/unix/syscall-template.S:84
	84	../sysdeps/unix/syscall-template.S: No such file or directory.
	(gdb) info proc map
	process 30676
	Mapped address spaces:

	          Start Addr           End Addr       Size     Offset objfile
	            0x400000           0x401000     0x1000        0x0 /FILES/cctf/skippingrope
	            0x600000           0x601000     0x1000        0x0 /FILES/cctf/skippingrope
	            0x601000           0x602000     0x1000     0x1000 /FILES/cctf/skippingrope
	      0x7ffff7a3a000     0x7ffff7bcf000   0x195000        0x0 /lib/x86_64-linux-gnu/libc-2.24.so
	      0x7ffff7bcf000     0x7ffff7dcf000   0x200000   0x195000 /lib/x86_64-linux-gnu/libc-2.24.so
	      0x7ffff7dcf000     0x7ffff7dd3000     0x4000   0x195000 /lib/x86_64-linux-gnu/libc-2.24.so
	      0x7ffff7dd3000     0x7ffff7dd5000     0x2000   0x199000 /lib/x86_64-linux-gnu/libc-2.24.so
	      0x7ffff7dd5000     0x7ffff7dd9000     0x4000        0x0 
	      0x7ffff7dd9000     0x7ffff7dfc000    0x23000        0x0 /lib/x86_64-linux-gnu/ld-2.24.so
	      0x7ffff7fe8000     0x7ffff7fea000     0x2000        0x0 
	      0x7ffff7ff3000     0x7ffff7ff5000     0x2000        0x0 
	      0x7ffff7ff5000     0x7ffff7ff8000     0x3000        0x0 
	      0x7ffff7ff8000     0x7ffff7ffa000     0x2000        0x0 [vvar]
	      0x7ffff7ffa000     0x7ffff7ffc000     0x2000        0x0 [vdso]
	      0x7ffff7ffc000     0x7ffff7ffd000     0x1000    0x23000 /lib/x86_64-linux-gnu/ld-2.24.so
	      0x7ffff7ffd000     0x7ffff7ffe000     0x1000    0x24000 /lib/x86_64-linux-gnu/ld-2.24.so
	      0x7ffff7ffe000     0x7ffff7fff000     0x1000        0x0 
	      0x7ffffffde000     0x7ffffffff000    0x21000        0x0 [stack]
	  0xffffffffff600000 0xffffffffff601000     0x1000        0x0 [vsyscall]
	
	(gdb) find 0x7ffff7a3a000, +0x195000,"/bin/sh"
	0x7ffff7b9b9f9
	1 pattern found.

	(gdb) find &execlp,+999999999,"/bin/sh"
	0x7ffff7b9b9f9
	warning: Unable to access 16000 bytes of target memory at 0x7ffff7bd6381, halting search.
	1 pattern found.
	
	(gdb) print execlp
	$1 = {<text variable, no debug info>} 0x7ffff7af2a60 <__GI_execlp>




## Flag

	??