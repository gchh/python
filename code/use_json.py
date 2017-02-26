import json
#序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
def student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
        }

s = Student('Bob', 20, 88)
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))
print(json.dumps(s.__dict__))

#反序列化
json_str=json.dumps(s,default=lambda obj:obj.__dict__)

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

print(json.loads(json_str,object_hook=dict2student))
