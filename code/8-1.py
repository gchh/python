#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    #__slots__ = ('name', 'age', 'set_age', 'score') #--@
    __slots__ = ('name', 'age', 'set_age', 'set_score') #--$ 用tuple定义允许绑定的属性名称

s=Student()
s.name='Michael'
print(s.name)

def set_age(self,age):
    self.age=age

from types import MethodType

s.set_age=MethodType(set_age,s)# 给实例绑定一个方法，否则会提示该实例无此方法

s.set_age(25)
print(s.age)
#且该方法只对s起作用，Student无此方法
#s2=Student()
#s2.set_age(25)
#print(s2.age)

def set_score(self, score):
    self.score = score

#Student.set_score=set_score #--@使用上个@则使用此@
Student.set_score=MethodType(set_score,Student) #--$使用上个$则使用此$

s.set_score(100)
print(s.score)

s2=Student()
s2.set_score(90)
print(s2.score)

#s2.city='Xiamen'

class GraduateStudent(Student):
    pass

g=GraduateStudent()
g.city ='Beijing'
print(g.city)
