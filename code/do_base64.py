import base64

c=base64.b64encode(b'binary\x00string')
print(c)
d=base64.b64decode(c)
print(d)

e=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e)
f=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(f)
g=base64.urlsafe_b64decode(f)
print(g)
