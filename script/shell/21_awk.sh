#!/bin/bash

# awk

# awk 'BEGIN{print "start"} pattern{commands} END{print "end"}' file
# 三个部分均是可选的
# 执行过程：
# 1）begin部分；读取文件
# 2）读一行，执行pattern部分；再读一行，再执行，循环
# 3）读到输入流末尾，执行end部分
# 通常，初始化放在BEGIN语句块，逻辑放在pattern语句块，打印或者输出结果放在END语句块

# 比如这里可以打印文件的行数目
awk 'BEGIN {i=0} {i++} END{print i}' ./cost/mapfile

# 使用不带参数的print时，会打印当前行
echo -e "line1\nline2" | awk 'BEGIN {print "Start"} {print} END{print "End"}'

# 只有pattern语句块
echo | awk '{var1="v1";var2="v2";print var1,var2}'

# awk的特殊变量
# NR Number of record, 记录号，相当于执行过程中的行号
# NF Number of fields, 当前行的字段数
# $0 当前行的文本内容
# $1 当前行的第一个字段
awk '{print "Line No:"NR", No of fields:"NF", $0="$0"，$1="$1""}' ./cost/cutfile
awk 'END{print NR}' ./cost/mapfile
