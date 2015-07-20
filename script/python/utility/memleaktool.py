#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import logging;logging.basicConfig(level = logging.INFO)

from map_generator import random_hex_str

def func_map_sort(map_file_path, sort_file_path):
	if not os.path.isfile(map_file_path):
		logging.warning('NO file named "%s" to read.' % map_file_path)		
	else:
		with open(map_file_path, 'r') as mf:
			func_map_list = mf.readlines()
			func_map_list.sort(key = lambda x:x[8:16])
			with open(sort_file_path, 'w') as tf:
				for line in func_map_list:
					tf.write(line)

def collect_stack_info(log_file, sorted_map_file):
	with open(sorted_map_file, 'r') as f:
		in_stack_info_area_flag = False
		str = ''
		lines = f.readlines()
		with open(log_file, 'r') as f:
			for line in f.readlines():
				if line[0:10] == 'CallStack:':
					in_stack_info_area_flag = True
					continue
				if in_stack_info_area_flag == True:				
					if line[0:4] == ' <--':
						str += func_addr_match(line[5:], lines)
					else:
						in_stack_info_area_flag = False
						str += '\n'
					print(str)
	return str
	

def func_addr_match(func_addr_str, sorted_map_list):
	low = 0
	high = len(sorted_map_list) - 1
	idx = -1
	while low <= high:
		mid = (low + high) // 2
		if low == high - 1:
			idx = high
			break
		elif func_addr_str[8:16] > sorted_map_list[mid][8:16]:
			low = mid
		elif func_addr_str[8:16] < sorted_map_list[mid][8:16]:
			high = mid
		elif func_addr_str[8:16] == sorted_map_list[mid][8:16]:
			idx = mid
			break
	print(sorted_map_list[idx])       
	return sorted_map_list[idx][17:]


if __name__ == '__main__':
	# func_map_sort('mapfile', 'sortedfile')
	# with open('sortedfile', 'r') as f:		
	# 	print(func_addr_match('00000000'+random_hex_str(8), f.readlines()))

	print(collect_stack_info('logfile', 'sortedfile'))





