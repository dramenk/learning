#!/bin/bash

# cat 拼接

# 拼接内容可以从文件中读取，拼接之后各个文件之间存在换行
echo -n "1. "
cat ./cost/file1 ./cost/file2

# 可以从标准输入中读取
echo "2. data in stdin." | cat

# 混合输入
echo "3. data in stdin." | cat - ./cost/file1

# 多个空白行压缩成单个
echo -n "4. "
cat -s ./cost/multiblanklines

# 显示行号
cat -n ./cost/multiblanklines
