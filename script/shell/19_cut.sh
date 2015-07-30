#!/bin/bash

# cut切分

# grep是按行取，cut是按列切分，默认的定界符(field delimiter)是制表符, -f为field，-f 1 剖出第一列
cut -f 1,4 ./cost/cutfile

# -d指定定界符
cut -f 1 -d ' ' ./cost/mapfile | head -5

# 只取第8到第12个字符
cut -c 8-12 ./cost/mapfile | head -5

# 取8-12 14-15两个区段的字符
cut -c 8-12,14-15 --output-delimiter=',' ./cost/mapfile | head -5
