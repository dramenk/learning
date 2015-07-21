#!/bin/bash

# 终端打印

# echo会自动添加换行; 参数-e表示支持转义序列，参数要写在要打印的字符串之前
echo -e "1.\tHello world!"
echo '2.Hello world!'
echo 3.Hello world!

# 三种形式各自存在一些特点或者说是限制：
var=hello
echo "4.${var}${notdefine}"		# 会打印var变量的具体内容,变量如果没有定义就什么都不返回
echo '5.${var}'					# 不求值，仅当作打印字符串
echo 6.hello;hello				# 出错，第二个hello被当作命令

# printf不会自动添加换行，支持格式化串
printf '7.\n'
printf "%-5s %-10s %-4s\n" No. Name Mark
printf "%-5s %-10s %-4s\n" 1 James 80.356

# 色彩输出,-n取消自动换行
echo -en "\e[1;31mRed \e[1;0m"	# \e[1;0m 表示颜色置回
echo -en "\e[1;32mGreen \e[1;0m"
echo -en "\e[1;33mYellow \e[1;0m"
echo -e "\e[1;34mBlue \e[1;0m"	
