from collections import namedtuple

Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print((p.x,p.y))
print(isinstance(p,Point))
print(isinstance(p,tuple))
print(isinstance(Point,tuple))

from collections import deque

L=['a','b','c']
q=deque(L)
q.append('x')
q.appendleft('y')
print(q)

q.pop()
q.popleft()
print(q)

from collections import defaultdict

dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

def f():
    return 'noo'
dd=defaultdict(f)
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict

d=dict([('a',1),('b',2),('c',3)])
print(d)
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)

od=OrderedDict()
od['z']=1
od['x']=2
od['y']=3
print(list(od.keys()))

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity= capacity

    def __setitem__(self,key,value):
        containsKey=1 if key in self else 0
        if len(self)-containsKey>=self._capacity:
            last=self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)
d=LastUpdatedOrderedDict(3)
d['a']=1
d['b']=2
d['c']=3
print(d)
d['d']=4
print(d)
d['b']=5
print(d)

from collections import Counter

c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c)
print(dict(c))
