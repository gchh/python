
n=10240099
#n=16777200
b1=(n&0xff000000)>>24
b2=(n&0xff0000)>>16
b3=(n&0xff00)>>8
b4=n&0xff
bs=bytes([b1,b2,b3,b4])
print(bs)

import struct

c=struct.pack('>IH',10240099,126)
print(c)
d=struct.unpack('>IH',c)
print(d)
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))



import struct

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'


print(struct.unpack('<ccIIIIIIHH', bmp_header))


import struct
def readBMP(fi):
    with open(fi, 'rb') as f:
        bit=f.read(30)
    return bit 
def judgeBMP(s):
    s1=struct.unpack('<ccIIIIIIHH', s)
    if s1[0]==b'B' and s1[1]==b'M':
        print('windows')
        print(s1[6],'*',s1[7],'---',s1[-1])
    elif s1[0]==b'B' and s1[1]==b'A':
        print('apple')
        print(s1[6],'*',s1[7],'---',s1[-1])
    else:
        print('false')

if __name__=='__main__':
    fname = input('请输入文件名称：')
    tx=readBMP(fname)
    judgeBMP(tx)
