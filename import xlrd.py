import os
import binascii

#file_name = "D:\\Users\\simon\\Downloads\\ransom\\aaa.txt"
file_name = "D:\\Users\\simon\\Downloads\\ransom\\login.xlsx.enc"
with open(file_name, 'rb') as f:
    content = f.read()
    f.close()
#content.encode('utf-8')
filehex=binascii.hexlify(content)
print(filehex)