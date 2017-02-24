class Animal(object):
    pass

#大类
class Mammal(Animal):
    def mammal(self):
        print('我是哺乳动物！')
    pass

class Bird(Animal):
    def bird(self):
        print('我是鸟儿！')    
    pass

#各种动物
class Dog(Mammal):
    def wow(self):
        print('狗吠......')
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


#能力
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

#食物
class CarnivorousMixIn(object):
    pass

class HerbivoresMixIn(object):
    pass

class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass

class Bat(Mammal,FlyableMixIn):
    pass

