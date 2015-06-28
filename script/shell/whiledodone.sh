#########################################################################
# File Name: whiledodone.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月12日 星期六 23时28分51秒
#########################################################################
#!/bin/bash

declare -i s=0

declare -i i=0

while [ "$i" != "100" ]
do
	i=i+1
	s=s+i
done

echo "Result is $s"

exit 0
