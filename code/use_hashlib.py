import hashlib

md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5=hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


sha1=hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha1=hashlib.sha1()
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


def get_md5(file):
    md5=hashlib.md5()
    md5.update(file.encode('utf-8'))
    return md5.hexdigest()
def calc_md5(user,password):
    return get_md5(password+user)
def cj_db(us,pw):
    #db={}
    db[us]=calc_md5(us,pw)
    return db
    
def login(user,password):  
    if user in db and (db[user]==get_md5(password+user) or db[user]==get_md5(password)):
        print('pass')
    else:
        print('用户名或密码错误')

if __name__=='__main__':
    db={
        'atdo':'e10adc3949ba59abbe56e057f20f883e',
        'gcu':'a152e841783914146e4bcd4f39100686',
        'gch':'e10adc3949ba59abbe56e057f20f883e'
        }    
    print('创建用户登录数据库')
    us=input('输入用户名：')
    pw=input('输入密码：')
    db=cj_db(us,pw)
    
    print('登录验证')
    user=input('用户名：')
    password=input('密码：')    
    login(user,password)
