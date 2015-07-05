#!/usr/bin/env python

print('a')
print '100+200=',100+200
print 'Now, type your key words, we\'ll list late:'
keywords=raw_input()
print 'The key words you input is:', keywords
print "nochange line.",
###############################################################
# list and tuple 
###############################################################
listA = ['a', 'b', 'c']
print listA
tupleB = ('a', 'b', 'c')
print tupleB

###############################################################
# if...elif...else... 
###############################################################
age=18
if age>18:
	print 'adult'
elif age>12:
	print 'young'
else:
	print 'child'

###############################################################
# loop
# there're two kinds of LOOP: 1)for...in...  2)while
###############################################################
sum = 0
for n in range(101):
	sum = sum + n
print sum

sum = 0
n = 1
while n <= 100:
	sum += n
	n += 1
print sum
