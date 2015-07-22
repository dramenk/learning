#!/bin/bash

# 打印

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
echo "8."
echo -en "\e[1;31mRed \e[1;0m"	# \e[1;0m 表示颜色置回
echo -en "\e[1;32mGreen \e[1;0m"
echo -en "\e[1;33mYellow \e[1;0m"
echo -e "\e[1;34mBlue \e[1;0m"

# 重定向，不会打印到屏幕仅仅打印到文件
# 0-stdin 1-stdout 2- stderr
echo "This is a sample text 1." > temp.log	# 会清空原有日志的内容
echo "This is a sample text 2." >> temp.log # 追加内容
echo "This is stdout." 1>> temp.log			# 1>>和>>是一样的
ls NotExistFile 2>> temp.log				# 打印错误的信息要使用2>或者2>>
ls NotExistFile 2> /dev/null				# 打印到黑洞
ls NotExistFile 2>> temp.log | cat -n		# stderr被重定向，就不再进入管道的stdin了，这条屏幕无输出
# tee重定向了stdout的副本，另一份数据作为了后续管道的stdin，因此下面一条打印会在文件和终端同时出现
# tee默认会覆盖文件，-a参数表示append追加
echo "This is a sample text3." | tee -a temp.log | cat

