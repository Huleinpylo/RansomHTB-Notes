import os

file_name = "D:\\Users\\simon\\Downloads\\ransom\\aaa.txt"

#f = open(file_name, "r")
#print(f.read())

 
0x5355504552534543 
0x5552455355504552 
0x5345435552455355 
0x5045525345435552 
0x4553555045525345 
0x4355524553555045 
0x5253454355524553 
0x5550455253454355 
0x5245535550455253 
0x4543555245535550 
0x4552534543555245 



import binascii
filename = "D:\\Users\\simon\\Downloads\\ransom\\login.xlsx.enc"
with open(filename, 'rb') as f:
    content = f.read()
filehex=binascii.hexlify(content)



print (type(filehex))
print (filehex[0])
print (filehex)

