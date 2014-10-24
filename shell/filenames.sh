#########################################################################
# File Name: filenames.sh
# Author: kelongwen
# mail: kelongwen@huawei.com
# Created Time: 2014年04月11日 星期五 23时30分25秒
#########################################################################
#!/bin/bash

echo -e "I will use 'touch' command to create 3 files."
read -p "Please input your filename: " fileuser

# 这里主要是测试一下，不让用户用空值
filename=${fileuser:-filename}

date1=`date --date='2 days ago' +%Y%m%d`
date2=`date --date='1 days ago' +%Y%m%d`
date3=`date +%Y%m%d`

filename1=${filename}${date1}
filename2=${filename}${date2}
filename3=${filename}${date3}

touch ${filename1}
touch ${filename2}
touch ${filename3}

exit 0
