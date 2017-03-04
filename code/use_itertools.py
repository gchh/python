import itertools

natuals=itertools.count(1)

for n in natuals:
    print(n)
    if n>=100:
        break


cs=itertools.cycle('abc')
a=0
for c in cs:
    print(c)
    a=a+1
    if a>=10:
        break

ns=itertools.repeat('A',5)
for n in ns:
    print(n)

natuals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))


for c in itertools.chain('ABC','123'):
    print(c)

for key,group in itertools.groupby('aabccbbbaaa'):
    print(key,list(group))

for key,group in itertools.groupby('AaBCcbBbaAa',lambda c:c.upper()):
    print(key,list(group))

natuals=itertools.count(1)
def pre(x):
    if x<=10:
        return True
    else:
        False
ns=itertools.takewhile(pre,natuals)
print(list(ns))
