from datetime import datetime,timedelta,timezone

now=datetime.now()#获取当前date time
print(now)
print(type(now))


#dt=datetime(2015,4,19,12,20)
dt=datetime(1970,2,1,0,0)
t=dt.timestamp()
print(t)
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))


cday=datetime.strptime('2017-3-2 23:22:45','%Y-%m-%d %H:%M:%S')
print(cday)
cday=datetime.strptime('2017.3.2 23:22:45','%Y.%m.%d %H:%M:%S')
print(cday)
cday=datetime.strptime('2017年3月2日23点22分45秒','%Y年%m月%d日%H点%M分%S秒')
print(cday)

dict={'Mon':'一','Tue':'二','Wed':'三','Thu':'四','Fri':'五','Sat':'六','Sun':'日'}
now=datetime.now()
w=now.strftime('%a,%b %d %H:%M')
print(w)
s=w[0:3]
print(s)
print(now.strftime('%Y年%m月%d日 星期dict[s] %H点%M分'))


now=datetime.now()
print(now)
t=now+timedelta(hours=1)
print(t)
t=now-timedelta(days=1)
print(t)
t=now-timedelta(days=1,hours=1)
print(t)


tz_utc_8=timezone(timedelta(hours=8))#创建时区UTC+8:00
now=datetime.now()
print(now)
dt=now.replace(tzinfo=tz_utc_8)#强制设置为UTC+8:00
print(dt)


utc_dt=datetime.utcnow()
print(utc_dt)
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
utc_dt=datetime.utcnow().astimezone(timezone(timedelta(hours=8)))
print(utc_dt)
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


'''
import datetime
now=datetime.datetime.now()#获取当前date time
print(now)
print(type(now))
'''
