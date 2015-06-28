#########################################################################
# File Name: Hello.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月11日 星期五 01时32分42秒
#########################################################################

# echo命令会自动加入换行
echo -e 'Hello world. \n'

# 脚本结束，如果exit 1，那么在bash中脚本执行完毕后，运行echo $?所得结果将是1
exit 0
