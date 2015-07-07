#!/usr/bin/python3

# python中，一个.py文件就可以称作一个模块
# 可以提高可维护性，可以避免函数和变量重名
# 模块重名可以通过“包”的机制来解决，就是一个包含__init__.py的目录结构。

' a test module '				# 文档注释

__author__ = 'Michael Liao'		

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('Hello, world!')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')
		
if __name__=='__main__':		# 如果模块是被导入，__name__的值为模块名字
	test()

# 模块内方法和变量的作用域：
# 正常的函数和变量名是公开的（public），可以被直接引用
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
# 但这只是约定，没有强制不让使用

# 如这样的抽象和封装：
def _private_1(name):
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

