#!/usr/bin/env python3
import random
import string

def random_alph_str(randomlength = 16):
	str = ''
	length = len(string.ascii_letters)
	while randomlength:
		str += string.ascii_letters[random.randint(0, length - 1)]
		randomlength = randomlength - 1
	return str

def random_hex_str(randomlength = 16):
	str = ''
	length = len(string.hexdigits[0:16])
	while randomlength:
		str += string.hexdigits[random.randint(0, length - 1)]
		randomlength -= 1
	return str 

if __name__ == '__main__':
	with open('mapfile', 'w') as f:
		for i in range(50000):
			f.write('00000000' + random_hex_str(8) + ' ' + random_alph_str(random.randint(16, 32)) + '\n')
