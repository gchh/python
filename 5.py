#-*- coding: utf-8 -*-
def normalize(name):
    return name[:1].upper()+name[1:].lower()
n=input('your name:')
L1=[]
L1.append(n)
L2=list(map(normalize,L1))
for x in range(len(L2)):
    print(L2[x])

from functools import reduce
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))  

from functools import reduce

#输入一串数字，并判断是否是整数或浮点数
l=input('输入数字:')
print('int or float :',isinstance(l,int) or isinstance(l,float))
print('string :',isinstance(l,str))

#将字符串转换成整数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
#print(str2int(l))

#将字符串转换成浮点数
def str2float(s):
    t=len(s)
    for x in range(0,len(s)):
        if s[x]=='.':
            t=x
            break
    s=[y for y in s if y!='.']
    return str2int(s)/(10**(len(s)-t))#如果直接用x，当输入不带小数点的整数时，输出却是整数/10得到的一个浮点数
print(str2float(l))
print('int or float :',isinstance(str2float(l),int) or isinstance(str2float(l),float))

#判断一个数是否是回数
def is_palindrome(n):
    #return str(n)==str(n)[::-1]
    #或者用下面的代码
    a,b=n,0
    while a:
        b=b*10+a%10
        a=int(a/10) #必须加上int()只保留结果的整数部分
    return(n==b)

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
