# GoGoGo
Reversing - 1000 points

## Challenge 
> Go get the password to this crackme!

> Creator -- quanyang (@quanyang)

> https://crossctf.dystopia.sg/files/b7fe2ee3cfffeb7696a503adc8db2b9d/crackme-linux-stripped.go

## Solution

    gdb ./crackme-linux-stripped.go 


    Reading symbols from ./crackme-linux-stripped.go...(no debugging symbols found)...done.
    (gdb) run
    Starting program: /FILES/cctf/crackme-linux-stripped.go 
    [New LWP 319]
    [New LWP 320]
    [New LWP 321]
    Welcome to CrossCTF 2018!
    Enter the password:
    ^C        
    Thread 1 "crackme-linux-s" received signal SIGINT, Interrupt.
    0x080a5041 in ?? ()
    (gdb) layout asm

	    0x80a5041       cmp    $0xfffff001,%eax                                    │
	   │0x80a5046       jbe    0x80a5064                                           │
	   │0x80a5048       movl   $0xffffffff,0x14(%esp)                              │
	   │0x80a5050       movl   $0x0,0x18(%esp)                                     │
	   │0x80a5058       neg    %eax                                                │
	   │0x80a505a       mov    %eax,0x1c(%esp)                                     │
	   │0x80a505e       call   0x80738a0                                           │
	   │0x80a5063       ret                                                        │
	   │0x80a5064       mov    %eax,0x14(%esp)                                     │
	   │0x80a5068       mov    %edx,0x18(%esp)                                     │
	   │0x80a506c       movl   $0x0,0x1c(%esp)                                     │
	   │0x80a5074       call   0x80738a0                                           │
	   │0x80a5079       ret            


Hopper decompiler

        ; Variables:
        ;    arg_18: int, 28
        ;    arg_14: int, 24
        ;    arg_10: int, 20
        ;    arg_C: int, 16
        ;    arg_8: int, 12
        ;    arg_4: int, 8
        ;    arg_0: int, 4


                 sub_80a5020:
    080a5020         call       sub_8073550                                         
    ; sub_8073550, CODE XREF=sub_80a4a30+56, sub_80a4af0+56, sub_80a4bc0+72, sub_80a4cb0+72, sub_80a4da0+56
    080a5025         movl       arg_0(%esp), %eax
    080a5029         movl       arg_4(%esp), %ebx
    080a502d         movl       arg_8(%esp), %ecx
    080a5031         movl       arg_C(%esp), %edx
    080a5035         movl       $0x0, %esi
    080a503a         movl       $0x0, %edi
    080a503f         intl       $0x80
    080a5041         cmpl       $0xfffff001, %eax
    080a5046         jbe        loc_80a5064

    080a5048         movl       $0xffffffff, arg_10(%esp)
    080a5050         movl       $0x0, arg_14(%esp)
    080a5058         negl       %eax
    080a505a         movl       %eax, arg_18(%esp)
    080a505e         call       sub_80738a0                                         ; sub_80738a0
    080a5063         ret
                            ; endp

                 loc_80a5064:
    080a5064         movl       %eax, arg_10(%esp)                                  ; CODE XREF=sub_80a5020+38
    080a5068         movl       %edx, arg_14(%esp)
    080a506c         movl       $0x0, arg_18(%esp)
    080a5074         call       sub_80738a0                                         ; sub_80738a0
    080a5079         ret
                            ; endp
    080a507a         db  0xcc ; '.'
    080a507b         db  0xcc ; '.'
    080a507c         db  0xcc ; '.'
    080a507d         db  0xcc ; '.'
    080a507e         db  0xcc ; '.'
    080a507f         db  0xcc ; '.'

Strings
	
	$ objdump -s -g crackme-linux-stripped.go > strings.txt

	 80ec4a0 36373430 37323236 35363235 54686520  674072265625The 
	 80ec4b0 666c6167 20697320 43726f73 73435446  flag is CrossCTF
	 80ec4c0 7b25587d 62616420 64656665 7220656e  {%X}bad defer en

flag string (`CrossCTF{%X}`) at address 0x80EC4AC

---

Search in disassembly, function `sub_80c3500`.

	$ objdump -D crackme-linux-stripped.go > disassembly.txt

	 80c37b3:	8d 05 ac c4 0e 08    	lea    0x80ec4ac,%eax


Adding a breakpoint in GDB: it is called only after entering our password. Hence is it the function for validate?

Some possible buffer strings?
    
    offset: value
    -152: 0x10325476
    -156: 0x98badcfe
    -160: 0xefcdab89
    -164: 0x67452301
    -172: 0x2532efdf
    -176: 0xbadbad21
    -180: 0xbe10fefa
    -184: 0xae1b10ae

    p32(0xae1b10ae) + p32(0xbe10fefa) + p32(0xbadbad21) + p32(0x2532efdf) + p32(0x67452301) + p32(0xefcdab89) + p32(0x98badcfe) + p32(0x10325476)


## Flag

	??