#!/bin/bash

#函数的调用和函数的定义有位置上的先后要求
#fname
function fname()
{
	echo "Hello world."
}
echo -n "1."
fname

function printit()
{
	# 函数内的$1同shell script的$1是不同的
	echo "Your choice is $1."			# $n 函数接收的第n个参数
	echo "All para are $@."				# $@ 或者 $* 接收所有参数
	return 1							# 返回值
}

# 函数是支持导出的，这样函数也能像环境变量一样扩展到子进程
export -f fname

# 分支结构
case $1 in
	"one")
		printit 1
		;;
	"two")
		printit 2
		;;
	"three")
		printit 3
		;;
	*)
		echo "Usage $0 {one|two|three})"
		;;
esac

# 可以通过$?获取上一个调用函数的返回值
echo "2.$?"

exit 0
