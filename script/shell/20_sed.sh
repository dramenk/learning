#!/bin/bash

# sed stream editor

# 常常用来查找替换
# 从文件中接收输入
# sed 's/pattern/replace_string/' file
# 从stdin中接收输入
# cat file | sed 's/pattern/replace_string/'

# 仅仅替换第一个匹配到的
echo 'thisthisthis' | sed 's/this/THIS/'
# 替换所有匹配到的
echo 'thisthisthis' | sed 's/this/THIS/g'
# 第n处匹配开始替换 
echo 'thisthisthis' | sed 's/this/THIS/2g'

# sed支持正则表达式
# /pattern/d表示删除模式串，这里就把空行给移除了
echo -e 'line1.\n\nline2.' | sed '/^$/d'

# 子串匹配
# 模式串放在()中间，这里\1表示第一个模式串
echo 'This is digit 7 and digit 18.' | sed 's/digit \([0-9]*\)/\1/g'
# 还有第二个模式串的例子
echo 'eight EIGHT' | sed 's/\([a-z]\{5\}\) \([A-Z]\+\)/\2 \1/g'
