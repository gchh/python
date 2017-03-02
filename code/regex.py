import re


test=input('输入：')
if re.match(r'^[a-zA-Z]*\s+\w{0,20}',test):
    print('OK')
else:
    print('failed')

