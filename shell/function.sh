#########################################################################
# File Name: function.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月12日 星期六 22时49分39秒
#########################################################################
#!/bin/bash

#函数的调用和函数的定义有位置上的先后要求
#fname

function fname()
{
	#code;
	echo "Hello world."
}

fname

########################################################################

function printit()
{
	# 函数内的$1同shell script的$1是不同的
	echo "Your choice is $1."
}

echo "This program will print your selection!"

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

exit 0
