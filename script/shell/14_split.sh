#!/bin/bash

# split分割

# -b bytes 按照文件大小分割
split -b 5k ./cost/mapfile

# -d 输出文件以数字为后缀，-a指定后缀长度
split -da 4 -b 5k ./cost/mapfile

# 再增加文件的目录和前缀名
split -da 4 -b 5k ./cost/mapfile output/splited_file

# -l line 按行分割文件
split -da 1 -l 100 ./cost/mapfile output/splited_line
