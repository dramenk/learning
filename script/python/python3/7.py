#!/usr/bin/python3

#### 对象与类 ####
class Student(object):	# 一般大写字母开头，object为父类
	dark = "Hide"				# 这是个类属性，类的所有实例都能访问

	# the first parameter of FUNCTION __init__ is always 'self', __init__ is default constractor.
	# variable __xx is private, and __xx__ is not private variable
	# we can use set or get function to set or get these variable
	def __init__(self, name, score):
		self.name = name		# 这是个实例属性，实例属性可以屏蔽同名的类属性，所以不要同名
		self.__privateName = name
		self.__score = score	# 其实时换了个名字：_Student__score
								# 区别__xxx__这样能够直接访问的特殊变量
	def print_score(self):
		print('%s: %s' % (self.name, self.__score))

	def print_name(self):
		print('%s' % self.name)


# 参数根据__init__写
bart = Student("dramenk", 90)

# python对象支持动态绑定属性
bart.weight = 65
print(bart.weight)
bart.print_score()

#### 继承/多态  ####
class Pupil(Student):
	def print_name(self):
		# print("pupil %s: %s" % (self.name, self.__score)) # private变量不继承
		print("pupil %s" % self.name)
	pass

class College_Student(Student):
	def print_name(self):
		# print("college student %s: %s" % (self.name, self.__score)) # private变量不继承
		print("college student %s" % self.name) # private变量不继承
	pass

pupil = Pupil("vod", 80)
college_student = College_Student("ked", 85)
pupil.print_name()
college_student.print_name()

print(isinstance(pupil, Student))
print(isinstance(pupil, Pupil))

#### 获取对象信息 ####
print(type(pupil)) 	# 获取对象类型
print(dir(pupil))	# 获取对象所有的属性和方法

# xxx(object)对应__xxx___方法
class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))

# getattr()、setattr()以及hasattr()
print(hasattr(dog, "x"))
setattr(dog, "x", 10)
print(getattr(dog, "y", 404))
