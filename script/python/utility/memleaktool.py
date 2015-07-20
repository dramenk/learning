#!/usr/bin/env python3
# -*- coding:utf-8 -*-

with open('mapfile', 'r') as mf:
	func_map_list = mf.readlines()
	func_map_list.sort(key = lambda x:x[8:16])
	with open('testfile', 'a') as tf:
		for line in func_map_list:
			tf.write(line)


