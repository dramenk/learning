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

