##将多个html文件合并成一个html文件
运行cmd  
假设保存网页文件夹"d:\123htm\"  
输入  
copy d:\123htm\*.html d:\123htm\all.htm  
d:\123htm\all.htm合并文件  

使用命令确实html文件合并文件何保留每文件文件名呢？


###或者：  
1.新建X.html文件；  
2.在X.html文件加入iframe标签例：  

	<iframe name="iframe1" marginwidth=0 marginheight=0 width=100% height=600 src="XXX.html文件(例：D:\a.html)" frameborder=0></iframe>
	<iframe name="iframe2" marginwidth=0 marginheight=0 width=100% height=600 src="XXX.html文件(例：D:\b.html)" frameborder=0></iframe>
	<iframe name="iframe3" marginwidth=0 marginheight=0 width=100% height=600 src="XXX.html文件(例：D:\c.html)" frameborder=0></iframe>  

上面两个方法效果一样