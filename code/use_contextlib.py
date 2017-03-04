try:
    f=open('d:/users/atdo/desktop/a2 Platinum.png','rb')
    print(f.read(30))
except FileNotFoundError as e:
    print('except:',e)
except UnicodeDecodeError as e:
    print('except:',e)
finally:
    try:
        if f:
            f.close()
    except NameError as e:
        print('except:',e)
    finally:
        print('finally')
        
with open('d:/users/atdo/desktop/a2 Platinum.png','rb') as f:
    print(f.read(30))


class Query(object):
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...'%self.name)

with Query('Bob') as q:
    print(q.query())


from contextlib import contextmanager

class Query(object):
    def __init__(self,name):
        self.name=name

    def query(self):
        print('Query info about %s...'%self.name)

@contextmanager
def create_query(name):
    print('Begin')
    r=Query(name)
    yield r
    print('End')

with create_query('Bob') as q:
    print(q.query())


@contextmanager
def tag(name):
    print("<%s>"%name)
    yield
    print("</%s>"%name)

with tag("h1"):
    print("hello")
    print('world')


from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    n=0
    for line in page:
        print(line)
        n=n+1
        if n>=10:
            break
print('*******************************')
@contextmanager
def  user_closing(thing):
    try:
        yield thing
    finally:
        thing.close()

with user_closing(urlopen('https://www.python.org')) as page:
    n=0
    for line in page:
        print(line)
        n=n+1
        if n>=10:
            break
