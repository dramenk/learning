#!/bin/bash

# tr 转换

# translate，tr只能通过stdin接收输入
# tr [optoins] tr1 tr2 ，tr1--->tr2是映射规则，tr按照映射规则，将输入映射成输出
echo "1. hello world." | tr 'a-z' 'A-Z'						# 这个规则可以用来加密和解密

# -d，删除规则，集合里面的字符都删除
echo -n "2. "
echo "hel1234l456o wor63456ld.7809" | tr -d '0-9'			# 删除数字

# -c，取补集
echo "3. he12l4lo2 34wor12l4d21.34" | tr -d -c '0-9 . \n'	# 删除除0-9，.，\n以外的字符

# -s，连续重复字符变成一个字符
echo "4. GNU is    not  Unix." | tr -s ' '					# 压缩空白字符
