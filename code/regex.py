import re


test=input('输入：')
if re.match(r'^[a-zA-Z]*\s+\w{0,20}',test):
    print('OK')
else:
    print('failed')

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())


t = '2-30'
m = re.match(r'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$', t)
print(m.groups())


email=input('输入Email:')
if re.match(r'[0-9a-zA-Z-.\_\s<>]+@[0-9a-zA-Z\_.-]+',email):
    print('ok')
    m=re.match(r'^(<)([0-9a-zA-Z-\_.\s]+)(>)\s*([0-9a-zA-Z-.\_\s@]+)$',email)
    if m:
        print(m.group(2))
    else:
        print('no name') 
else:
    print('failed')
