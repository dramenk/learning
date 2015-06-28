#########################################################################
# File Name: ifthen.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月12日 星期六 23时15分04秒
#########################################################################
#!/bin/bash

declare -i tmp=$1

if [ "$tmp" == "5" ] 
then
	echo '$1 is 5'
else
	echo '$1 is not 5'
fi

exit 0
