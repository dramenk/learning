#########################################################################
# File Name: ifthen.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月12日 星期六 23时15分04秒
#########################################################################
#!/bin/bash

# 比较测试/条件分支

declare -i tmp=$1

# if...then...elif...then...else...fi
if [ "$tmp" == "5" ] 
then
	echo '$1 is 5'
elif [ "$tmp" == "6" ]
then
	echo '$1 is 6'
else
	echo '$1 is not 5'
fi

# if条件判断比较长，可以通过逻辑运算符精简
# 条件为真执行
[ ${tmp} -eq "5" ] && echo '$1 is 5'
# 条件为假执行
[ ${tmp} -eq "5" ] || echo '$1 is not 5'

# 注意比较运算时，[ ... ]要注意留空格
[ ${tmp} -gt "5" ] && echo '$1 > 5'						# gt --> greater then (大于)
[ ${tmp} -lt "5" ] && echo '$1 < 5'						# lt --> little then  (小于)
[ ${tmp} -ge "5" ] && echo '$1 >= 5'					# ge --> greater equal(大于等于)
[ ${tmp} -le "5" ] && echo '$1 <= 5'					# le --> little equal (小于等于)

file_var="./09_ifthen.sh"
[ -f ${file_var} ] && echo "${file_var} is a file." 	# 如果是文件或文件路径
[ -x ${file_var} ] && echo "${file_var} is executable"	# 如果文件可执行
[ -e ${file_var} ] && echo "${file_var} is exist."		# 如果文件存在
dir_var="/bin"
[ -d ${dir_var} ] && echo "${dir_var} is a directory."	# 如果是文件目录
exit 0
