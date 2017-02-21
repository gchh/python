class Student(object):
    def __init__(self,name):
        self.name=name

s=Student('Bob')
s.score=90
print(s.__dict__)

del s.score
print(s.__dict__)

class Student1(object):
    name ='Student'
    
p=Student1()
print(p.name) #打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student1.name) #打印类的name属性

p.name='Micheal'#给实例绑定name属性

print(p.name)
print(Student1.name) 

del p.name#删除实例的name属性
print(p.name)#再次调用p.name，由于实例的name属性没有找到，类的name属性就显示出来了

p.score=89
print(p.score)

del p.score
#print(p.score)

# 学生
class Student(object):
    # 用于记录已经注册学生数
    student_number = 0
    def __init__(self, name):
        self.name = name

# 注册一个学生:注册必填项名字，选填项利用关键字参数传递。注册完成，学生数+1
def register(name, **kw):
    a = Student(name)
    for k, v in kw.items():
        setattr(a, k, v)
    Student.student_number += 1
    return a
bob = register('Bob', score=90)
ah = register('Ah', age=8)
ht = register('ht', age=8, score=90, city='Beijing')

print(getattr(bob, 'score'))
print(getattr(ah, 'age'))
print(ht.city)
print(ht.__dict__)
print(Student.student_number)
