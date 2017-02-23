class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name: %s)'%self.name
    __repr__=__str__

print(Student('Michael'))

s=Student('Michael')
print(s)


class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a

    def __getitem__(self,y):
        m,n=1,1
        for x in range(y):
            m,n=n,m+n
        return m
    
for n in Fib():
    print(n)
print(Fib()[2])

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n,int): 
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b

            return L

print(Fib2()[2:10])

class Fib3(object):
    def __getitem__(self, n):
        a, b = 1, 1
        L=[]
        if isinstance(n,int):
            start=0
            stop=n
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0            
            
        for x in range(stop):
            if x>=start:
                L.append(a)            
            a, b = b, a + b
        if isinstance(n,int):
            return a
        if isinstance(n,slice):
            return L

print(Fib3()[:10])

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self,attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda:25
        return AttributeError('\'Student\' object has no attribute \'%s\''%attr)

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)

class Student(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s.'%self.name)

s=Student('Michael')
s.__call__()
s()
print(callable(s))
