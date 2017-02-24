from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
	
m=Month
print(m(1))
print(m['Feb'])
n=Month(1)
print(n)
print(n.value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
day1 = Weekday(1)
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday['Tue'].value)
print(Weekday(2).value)
print(day1==Weekday.Mon)
print(day1==Weekday.Tue)
#print(Weekday(7))
for a,b in Weekday.__members__.items():
    print(a,'=>',b,':',b.value)
# 另一种遍历枚举的方法
for weekday in Weekday:
    print('%s => %s' %(weekday.name,weekday.value))


from enum import Enum

Month = Enum('Month', 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec')

for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
