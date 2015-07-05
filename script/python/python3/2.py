#!/usr/bin/python3.4

# 定义函数
def my_abs(x):
	# 参数个数检查可以自动完成，但是参数类型检查需要这样：
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x > 0:
		return x
	else:
		return -x

# 空函数
def nop():
	pass

# 函数本身也是第一类值
a = my_abs

# 函数调用
print("my_abs(-6)", a(-6))

# 支持默认参数
# 必选参数在前，默认参数在后，否则Python的解释器会报错；
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小
# 的参数就可以作为默认参数。只有与默认参数不符时才需要提供额外的信息。
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print("power(6)", power(6))

# 支持可变参数，参数个数可变
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1, 2, 3, 4))



