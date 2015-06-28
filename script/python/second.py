#!/usr/bin/env python
import pdb

#########################################################
# dict
#########################################################
dictA = {'xiaoming':95, 'xiaoqiang':93}
print dictA

dictA['kelongwen'] = 95
print dictA

dictA.pop('kelongwen')
print dictA

#########################################################
# function
#########################################################
def nop():
	pass

def power(x, n = 2):
	loop = 1
	returnValue = x
	while (loop < n):
		returnValue *= x
		#pdb.set_trace()
		loop += 1
	return returnValue

print power(5)
print power(5, 5)
