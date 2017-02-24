#杨辉三角
#-*- coding: utf-8 -*-
def triangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
#第一次循环执行 yield L,输出[1]

#第二次循环执行 yield L 之后的语句 L.append(0)后，L =[1，0[，再执行后面的语句 L = [L[i - 1] + L[i] for i in range(len(L))] 此时L =【1，1】（i=0时 L[- 1] + L[0]为1，i =1时 L[0] + L[1]为1）直到再次遇到yield L语句，输出【1，1】

#第三次循环执行 yield L 之后的语句 L.append(0)后，L =[1，1，0]，再执行后面的语句 L = [L[i - 1] + L[i] for i in range(len(L))] 此时L =【1，2，1】（i=0时 L[- 1] + L[0]为1，i =1时 L[0] + L[1]为2，i=2时，L[1] + L[2]为1）直到再次遇到yield L语句，输出【1，2，1】

#后面以此类推
n=0
for t in triangles():
    print(t)
    n=n+1
    if n==10:
        break

