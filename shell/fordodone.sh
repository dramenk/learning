#########################################################################
# File Name: fordodone.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月12日 星期六 23时40分53秒
#########################################################################
#!/bin/bash

network="192.168.3"

for sitenu in `seq 1 20`
do
	ping -c 1 -w 1 ${network}.${sitenu} &> /dev/null && result=0 || result=1
	if [ "$result" == "0" ] ; then
		echo "Server $network.$sitenu is UP."
	else
		echo "Server $network.$sitenu is DOWN."
	fi
done
