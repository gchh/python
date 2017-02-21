#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=Myobject()

print(hasattr(obj,'x')) #是否有'x'属性
print(obj.x)

print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)

print(getattr(obj,'z',404)) # 获取属性'z'，如果不存在，返回默认值404

print(hasattr(obj,'power'))
print(getattr(obj,'power'))
print(obj.power)
print(obj.power())

fn=getattr(obj,'power')
print(fn)
print(fn())

print(hasattr(obj,'__init__'))
print(getattr(obj,'__init__'))
print(obj.__init__())

sum=obj.x+obj.y
print(sum)
sum=getattr(obj,'x')+getattr(obj,'y',100)
print(sum)
sum=getattr(obj,'x')+getattr(obj,'z',100)
print(sum)

print(dir(obj))

def xffsa(fp):
    if hasattr(fp,'z'):
        return fp.power()
    else:
        return '%s 没有\'x\'属性'%fp

print(xffsa(obj))

#用callable()判断哪些属性是方法
print(callable(obj.x))
print(callable(obj.power))
print(callable(xffsa))
