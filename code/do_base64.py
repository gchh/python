import base64

c=base64.b64encode(b'binary\x00string')
print(c)
d=base64.b64decode(c)
print(d)
