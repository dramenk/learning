#!/bin/bash

# 数组array 和 关联数组ass_array

# 数组变量定义，下标从0开始，个元素以空格分开，不要写成(1, 2, 3, 4)，否则array[0]为“1,”
array_var=(1 2 3 4 5)
index=0
array_var[$index]="2"
echo "1.${array_var[$index]}"
echo "2.${array_var[*]} | ${array_var[@]}"		# 打印数组所有值
echo "3.${array_var}"							# 这样打印的只是数组的第一个值
echo "4.${#array_var[*]}"						# 数组长度

# 关联数组就是其他语言中的map，映射，下标非数字，而是字符串。其声明：
declare -A ass_array
# 赋值：
ass_array=(["name"]="LiMing" ["age"]=25)
ass_array["score"]=98
echo "5.${ass_array[*]}"						# 取值
echo "6.${!ass_array[*]}"						# 取索引

