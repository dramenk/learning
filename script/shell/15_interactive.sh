#!/bin/bash

# 自动交互

# 自动发送
echo -e "ke\nlongwen\nabcking" | ./07_read.sh

echo '----------------------------------------'

# 从文件发送
echo -e "ke\nlongwen\nABCking" > tmpfile
./07_read.sh < tmpfile
rm -f tmpfile
