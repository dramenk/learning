#!/usr/bin/python3
from functools import reduce

print("高阶函数英文叫Higher-order function. 函数本身就是一等公民，可以作为入参传入高阶函数中。")

# 比如inbuild函数map
# map()函数接收两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	return x*x
a = map(f, range(10))
print(a) 						# 注意返回的结果是惰性序列
print("所有元素：", list(a))	# 利用list计算出所有的Iterator的元素

# 在比如reduce函数
# reduce接受一个函数和一个序列，这个函数必须接收两个参数，reduce把结果继
# 续和序列的下一个元素做累积计算
def add(x, y):
	return x + y
print("使用reduce计算1+...+100=", reduce(add, range(101)))

# 假如没有python的int()函数
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# filter()也接收一个函数和一个序列, 通过作用于每个元素返回true/false来过滤元素
def is_odd(n):
	return n % 2 == 1
b = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]) # 也是Iterator
print(list(b))

# sorted()函数
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print("返回函数也是OK的")

# 这里是一个闭包，内部函数sum可以引用外部工厂lazy_sum的参数和局部变量，当
# lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
def lazy_sum(args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum
f1 = lazy_sum([1,2,3,4,5])
f2 = lazy_sum([1,2,3,4,5])
print(f1, f2)
print(f1==f2)					# false，f1和f2调用的结果相互不影响
print(lazy_sum([1,2,3,4,5])())

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs					# 返回的闭包的一个list
c1, c2, c3 = count()
print(c1())						# 不是1
print(c2())						# 不是4
