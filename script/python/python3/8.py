#!/usr/bin/python3

from types import MethodType
from enum import Enum
import hello

class Student(object):
	# 限制只能绑定name age属性或者方法，对继承子类不生效
	# __slots__ = ('name', 'age')
	
	# 属性化的get方法
	@property
	def age(self):
		return self._age
	# 属性化的set方法
	@age.setter
	def age(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._age = value

student = Student()

# 动态绑定实例属性
student.name = "gramenk"

def set_score(self, score):
	self.score = score

# 动态绑定实例方法
student.set_score = MethodType(set_score, student)
student.set_score(90)

# 还可以给类绑定方法, 这样类的所有实例都能使用set_score方法了
Student.set_score = MethodType(set_score, Student)
student1 = Student()
student1.set_score(77)

# 使用属性化的set方法
# student.age = 999
student.age = 28
print(student.age)

# python的class支持多重继承，Mixin的设计在于通过继承多个父类的能力
# 混入额外的功能

# 枚举类
# Month是Enum对象的一个实例，这个实例是一个“枚举类型”
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan, Month.Feb)

h = hello.Hello()
h.hello()
