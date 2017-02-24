#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

age=10
if age>=18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')


age=5
if age>=6:
    print('teenager')
    if age>=18:
        print('adult')
    else:
        print('teenager or kid')
else:
    print('kid')

print('BMI')
height=int(input('你的身高(cm)：'))
weight=int(input('你的体重(0.1kg)：'))
height/=100
weight/=10
bmi = weight/(height*height)
print('BMI=',bmi)
print('BMI= %.2f'%bmi)
if bmi<18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')
