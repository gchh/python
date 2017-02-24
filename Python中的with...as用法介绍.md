##Python中的with...as用法介绍
这个语法是用来代替传统的`try...finally`语法的。   
代码如下:

	with EXPRESSION [ as VARIABLE] WITH-BLOCK  
基本思想是with所求值的对象必须有一个`__enter__()`方法，一个`__exit__()`方法。  
紧跟with后面的语句被求值后，返回对象的`__enter__()`方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的`__exit__()`方法。  
代码如下:

	file = open("/tmp/foo.txt")
	try:
	    data = file.read()
	finally:
	    file.close()

使用`with...as...`的方式替换，修改后的代码是：  
代码如下:

	with open("/tmp/foo.txt") as file:
	    data = file.read()
	#!/usr/bin/env python
	# with_example01.py
	 
	 
	class Sample:
	    def __enter__(self):
	        print "In __enter__()"
	        return "Foo"
	 
	    def __exit__(self, type, value, trace):
	        print "In __exit__()"
	 
	 
	def get_sample():
	    return Sample()
	 
	 
	with get_sample() as sample:
	    print "sample:", sample

执行结果为  
代码如下:

	In __enter__()
	sample: Foo
	In __exit__()

1. `__enter__()`方法被执行
2. `__enter__()`方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
3. 执行代码块，打印变量"sample"的值为 "Foo"
4. `__exit__()`方法被调用with真正强大之处是它可以处理异常。可能你已经注意到Sample类的`__exit__`方法有三个参数- val, type 和 trace。这些参数在异常处理中相当有用。我们来改一下代码，看看具体如何工作的。  
5. 