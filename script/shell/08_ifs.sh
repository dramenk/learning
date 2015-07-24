#!/bin/bash

# IFS，internal field separator，内部字段定界府

# root:x:0:0:root:/root:/bin/bash
line=`cat /etc/passwd | grep root | head -1`

# IFS是处理定界符的环境变量
oldIFS=${IFS}
IFS=":"

count=0

for item in ${line}
do
	[ ${count} -eq 0 ] && user=${item} 
	[ ${count} -eq 6 ] && shell=${item}
	let count++
done
IFS=${oldIFS}

echo "$user's shell is $shell."
