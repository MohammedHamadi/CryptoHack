flag = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# flag = [flag[i:i+2] for i in range(0, len(flag), 2)]
# print("".join([chr(int(i,16))  for i in flag]))

# alternative solution

flagBytes = bytes.fromhex(flag)

print("".join([chr(i) for i in flagBytes]))