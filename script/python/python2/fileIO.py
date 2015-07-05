import os

try:
	with open('/home/kelongwen/Project/python_project/third.py', 'r') as f:
		for line in f.readlines():
			print line.strip()
except IOError, e:
	print 'except:', e


try:
	with open('/home/kelongwen/Project/python_project/chn.txt', 'r') as f:
		for line in f.readlines():
			print line.strip()
except IOError, e:
	print 'except:', e

with open('/home/kelongwen/Project/python_project/text.txt', 'w') as f:
	f.write('kelongwen')


#####
pathkelongwen = os.path.join(os.path.abspath('.'), 'kelongwen')
try:
	os.mkdir(pathkelongwen)
except OSError, e:
	os.rmdir(pathkelongwen)

print os.path.split(os.path.abspath('.'))[0]
print os.path.split(os.path.abspath('.'))[1]

print os.path.splitext('\path\kelongwen.txt')