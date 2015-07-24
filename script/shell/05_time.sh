#!/bin/bash

# 日期/时间/延时

begin=`date +%s`									# 读取命令序列的输出，还有$(...)
date +%s											# Posix时间戳，1970.01.01 00:00
date --date "Thu Jul 23 02:17:59 CST 2015" +%s		# --date表示提供日期串作为输入
date "+%Y %B %d"									# 格式化：年月日

sleep 2												# 延时
end=$(date +%s)
let past=$end-$begin
echo "The script costs $past seconds."
