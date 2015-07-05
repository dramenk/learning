#!/usr/bin/env python 

class student(object):
	# the first parameter of FUNCTION __init__ is always 'self', __init__ is default constractor.
	# variable __xx is private, and __xx__ is not private variable
	# we can use set or get function to set or get these variable
	def __init__(self, name, score):
		self.name = name
		self.__privateName = name
		self.__score = score

	def print_score(self):
		print self.__score

	def __high__(self):
		return 175

bart = student("kelongwen", 90)

print bart.name
#print bart.__privateName

bart.print_score()

class colleage_student(student):
	pass

colleage_bart = colleage_student("kelongwen", 99)
print colleage_bart.name
#print colleage_bart.__privateName
colleage_bart.print_score()

print high(bart)
