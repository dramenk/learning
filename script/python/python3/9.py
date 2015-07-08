#!/usr/bin/python3

#### 错误处理 ####

# try语句块如果执行出错，则后续代码不会继续执行，而是直接跳转至错误
# 处理代码，即except语句块；如果有finally语句块，finally语句块一定会
# 被执行。
try:
	print('try...')
	r = 10 / 0
	print('result:', r)
# 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语
# 句块捕获处理。
# Python的错误其实也是class，所有的错误类型都继承自BaseException，在
# 使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一
# 网打尽”。
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
	print('END')

# try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
# 内层函数抛出的错误可以由外层函数捕获，如果一直没有被捕获，那
# 最终python解释器会捕获到
