#try...except...finally...
try:
    print('try...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')


a=input('输入：')
try:
    print('try...')
    r=10/int(a)
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    a=input('输入：')
    try:
        b=bar(a)
        print(b)
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()
