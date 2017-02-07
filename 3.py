#计算圆面积
def area_of_circle(x):
    s=3.14*x*x
    return s
def c():
    r=float(input('输入该圆半径：'))
    c=area_of_circle(r)
    print('该圆面积是：',c)
    print('该圆面积是：%f'%c)
    print('该圆面积是：%.2f'%c)
    return
#求和
def summ(min,max):
    sum=0
    for i in range(min,max+1):
        sum+=i
    return sum
def s():
    min=int(input('输入求和起始数据：'))
    max=int(input('输入求和结束数据：'))
    s=summ(min,max)
    print('%d和%d之间（包括）的数据求和结果是：%d'%(min,max,s))
    return
#是否结束
def ssccdd():
    key=input('是否结束：y/n\n')
    if key=='y':
        print('结束')
    elif key=='n':
        print('继续')
        c()
        s()
        ssccdd()
    else:
        print('输入错误，重新输入\n')
        ssccdd()
    return
c()
s()
ssccdd()
