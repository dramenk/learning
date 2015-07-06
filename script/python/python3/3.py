#!/usr/bin/python3.4
import collections
import os

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print("L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']")

print(L[0:3])	# 0到3但不包括3
print(L[:3])	# 0可以省略
print(L[0:3:2])	# 步长为2

print(L[-2:])	# 从后往前
print(L[-2:-1]) # 从-2到-1（最后一个），但是不包括-1

print((1, 2, 3, 4, 5)[0:3])	# tuple能切片
print('ABCDEF'[0:3])		# 字符串能切片

# 迭代
print('"ABCD"可迭代？', isinstance('ABCD', collections.Iterable)) # 判断是否可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
	print(k)

# 列表生成式
a = [x * x for x in range(11)]
print(a)
a = [x * x for x in range(11) if x % 2 == 0] # 还可以增加限制条件
print(a)
print([d for d in os.listdir('.')])

# 生成器，不存储完整的列表，而是一边循环一边计算。
b = (x * x for x in range(11))
print(b)
print(next(b)) # 通过next()获取下一个值
print(next(b)) 
for n in b:
	print(n)

# 利用yield，类似于lua的coroutine，在yield出中断，在yield处继续
print("斐波拉契:")
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
for n in fib(5):
	print(n)

# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print("fib(10)是迭代器？", isinstance(fib(10), collections.Iterator))
print("fib(10)可迭代？", isinstance(fib(10), collections.Iterable))

