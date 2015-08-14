#!/usr/bin/python3.4

# 注释
print("python3 默认采用unicode，支持中文字符和字符串")

print("-----------------------字符串/编码--------------------------")
# 中文字符,单个字符与编码的对应关系可以通过下面两个转换获知：
print("'66'对应的字符：", chr(66))
print("'中'对应的编码：", ord('中'))

# 中文字符串，字符串类型是str，在内存中以unicode表示，以unicode为
# 基准，encode编码为byte，byte解码decode为unicode。
# 编解码方法有ascii；有utf-8
print(b'ABC'.decode('ascii'))
print("中文字符".encode('utf-8'))

print("------------------------类型与值----------------------------")
a = 20
b = 10
print("b - a =", float(a) - float(b))

print("-----------------------list/tuple---------------------------")
classmates = ['Michael', 'Bob', 'Tracy']
classmates.append("Gramenk") 	# 增，list类型是有序表
print(classmates)
classmates.pop(0)				# 删，下标从0开始 
print(classmates)
print('list是有序表，支持排序：', classmates.sort())		# 排序
classmates[1] = 228646			# 改, 元素类型可以多样
print(classmates[1])			# 查
print("len of classmates is:", len(classmates))
# 一个元素的元组的定义
tupleConOne = (1,)

print("----------------------if-elif-else--------------------------")
age = int(input("请输入年龄："))
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

print("-------------------------loops------------------------------")
# for
sum = 0 
for value in range(101):
	sum += value
print("1 + ... + 100 =", sum)

# while
sum, n = 0, 1
while n <= 100:
	sum += n
	n += 1
print("1 + ... + 100 =", sum)

print("------------------------dict/set-----------------------------")
# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Gramenk'] = 90
print(d['Gramenk'])		# 如果没有，抛出错误
d.pop('Gramenk')
print(d.get('Gramenk')) # 如果没有，返回None

#set
s1 = set([1, 1, 2, 3])	# 以有序表list构造无序集合set，重复元素自动过滤
print(s1)
s1.add(4)				# set.add(key)
print(s1)
s1.remove(4)			# set.remove(key)
print(s1)
s2 = set([2, 3, 10])
print(s1 & s2)			# 交集
print(s1 | s2)			# 并集


