#!/bin/bash

# 变量

# 脚本语言一般都是动态类型，即使用前不需要声明类型；bash shell更特殊，所有变量的值都是字符串
var1=1							# 注意=号两边不要加空格，否则var1会被当作command处理
var2='23456789'

# $... 和 ${...} 可以取值
echo "$var1${var2}"

# 环境变量：
# 当前进程没有定义，而是从父进程继承而来的变量。设定为环境变量之后，当前脚本执行的任何程序都
# 会继承这个变量。
# export能够设定一个变量为环境变量。
# env能够获取当前bash的环境变量。
export var1
env | grep var1

# 子shell
pwd
(cd /opt;ls)					# 子shell的操作不影响当前shell
pwd

# 补充：
echo ${#var2}					# 取变量的字符串长度
echo $SHELL						# 获取shell类型

if [ $UID == 0 ]; then
	echo "Super user."
else
	echo "Non root user."
fi
