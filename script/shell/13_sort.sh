#!/bin/bash

# sort

# sort能够对stdin和文件进行排序
echo '1) ';sort ./cost/file* ./cost/multiblanklines

# -n 按照数字排序
# -r 逆序排序
# -k num，按照第num列排序
echo '2) 按照第一列逆序数字排序';sort -nrk 1 ./cost/data1
echo '3) 按照第二列排序';sort -k 2 ./cost/data1

# uniq从stdin和文件中提取单一的行
echo '4) 排序后只提取单一的行';sort ./cost/* | uniq
