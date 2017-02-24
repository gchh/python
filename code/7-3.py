#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Fish(Animal):
    def run(self):
        super().run() #父类run()方法
        print('Fish is swimming...')

def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class Timer(object):
    def run(self):
        print('Start...')
        
a = Animal()
b = Dog()
c = Cat()
d = Tortoise()
e = Timer()
f = Fish()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('b is Animal?', isinstance(d, Animal))
print('b is Dog?', isinstance(b, Dog))
print('b is Cat?', isinstance(b, Cat))

run_twice(a)
run_twice(b)
run_twice(c)
run_twice(d)
run_twice(e)
f.run()
Animal().run()
