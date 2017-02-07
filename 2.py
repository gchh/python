sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
#计算1-100的整数和
sum=0
for x in range(101):
    sum+=x
print(sum)
#计算100以内的奇数和
sum=0
n=1
while n<100:
    sum+=n
    n=n+2
print(sum)
#计算100以内的偶数和
sum=0
n=0
while n<=100:
    sum+=n
    n=n+2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
n=0
while n<len(L):
    print('Hello,',L[n])
    n+=1
print('********')
for name in L:
    print('Hello,',name)
    print('Hello,%s'%name)
