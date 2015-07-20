#!/usr/bin/env python3

import random
import string

from map_generator import random_hex_str

def random_log(randomlength=8):
	a = ''
	for i in range(randomlength // len(string.ascii_letters) + 1):
		a += string.ascii_letters
	b = list(a)
	random.shuffle(b)
	return ''.join(b[:randomlength])

def leaklog_keyword():
	return 'CallStack:\n'

def random_func_log():
	return ' <-- ' + '00000000' + random_hex_str(8) + '\n'

def random_stack_log():
	str = ''
	for i in range(random.randint(5, 15)):
		str += random_func_log()
	return str

if __name__ == '__main__':
	with open('logfile', 'w') as f:
		for i in range(50000):
			if random.uniform(0, 1) < 0.0005:
				f.write(leaklog_keyword() + random_stack_log())
			f.write(random_log(random.randint(100, 150)) + '\n')
