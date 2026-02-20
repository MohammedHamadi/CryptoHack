flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
flag_format = "crypto{1"
flag = bytes.fromhex(flag)
key = [flag[i] ^ ord(flag_format[i]) for  i in range(len(flag_format))]

text = [chr(flag[i]^key[i%len(key)]) for i in range(len(flag))]
print("".join(text))
