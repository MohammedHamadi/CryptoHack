flag = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag = bytes.fromhex(flag)
favourite_byte = int(flag[0]) ^ ord("c")

print(''.join([chr(i^favourite_byte) for i in flag]))/