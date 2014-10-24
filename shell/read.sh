#########################################################################
# File Name: read.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月11日 星期五 01时42分28秒
#########################################################################
#!/bin/bash


# 这里的fn和ln在外层的bash是echo不出来的，因为fn和ln都没有export到环境变量上去
echo 'Please input the first name:'
read fn

echo 'Please input the last name:'
read ln

# echo -e 'Name is $fn $ln'
# 这里要注意一下：不要像上面这样用单引号，不然会直接输出$fn和$ln
echo -e "Name is $fn $ln"

exit 0
