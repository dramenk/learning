#!/usr/bin/python3
import os
import shutil
import pickle

try:
	f = open('./hello.py', 'r')
	print(f.read())
finally:
	if f:
		f.close()

# 上面的可以改写为：
# 利用with语句，自动调用close方法
with open('./hello.py', 'r') as f:
	print(f.read())

with open('./hello.py', 'r') as f:
	print(f.read(10))				# 一次读取一点，免得内存爆掉

with open('./hello.py', 'r') as f:
	print(f.readlines())			# 如果是配置文件，可以一行一行的读

# file-like object: 只要有read()方法

# 读二进制文件
with open('./test.png', 'rb') as f:
	print(f.read(20))

with open('./gbkfile.txt', 'r', encoding='gbk', errors='ignore') as f:
	print(f.read())

# 写文件,write时一般不会立刻写，空闲时慢慢写；close时一定会写完
with open('./filew.txt', 'w', encoding='gbk') as f:
	f.write("你好。")

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
# (略)

# Python内置的os模块可以直接调用操作系统提供的接口函数
print(os.name)		# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.uname())	# 系统的详细信息
print(os.environ)	# 环境变量
print(os.environ.get('PATH'))

dirstr = os.path.join(os.path.abspath('.'), 'testdir')	# join可以正确处理系统的路径分隔符
os.mkdir(dirstr)
os.rmdir(dirstr)
os.rename('./filew.txt', './filew.v')
os.remove('./filew.v')

# os模块下没有cp函数，不过shutil模块提供了copyfile()的函数
shutil.copyfile('./test.png', './test1.png')
os.remove('./test1.png')

# 过滤文件
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 序列化：把变量从内存中变成可存储或传输的过程，反之为反序列化
# Python的序列化pickle
d = dict(name='Bob', age=13, score=93)
with open('./pickleFile.pkl', 'wb') as f:
	pickle.dump(d, f)

with open('./pickleFile.pkl', 'rb') as f:
	print(pickle.load(f))
