#!/bin/bash

# 数学运算

# 虽然bash shell的变量都是以字符形式存储，但是可以利用let, (()), []进行数学运算
no1=1
no2=2
let result=no1+no2
echo "1.${result}"
let result--
echo "2.${result}"
let result+=2
echo "3.${result}"

# 如果要应用到浮点数，就需要bc计算器
result=`echo "0.56*${result}" | bc`
echo "4.${result}"

result=`echo "scale=2;3/8" | bc`		# 精确到两位小数
echo "5.${result}"

echo "6."
echo "obase=2;100" | bc					# 二进制输出
echo "obase=2;ibase=8;100" | bc			# 二进制输出，八进制输入
echo "10^10" | bc						# 10的10次方
