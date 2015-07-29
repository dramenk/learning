#!/bin/bash

# grep

# 从文件中接收。
# -o表示仅仅列出匹配部分，非整行列出；-i表示忽略大小写。
echo '1. '
grep -oi --color=auto 'hello' * 2> /dev/null

# 从stdin中接收
echo '2. '
echo 'hello world.' | grep --color=auto hello

# -E表示支持正则表达式,-R表示递归查找,-n表示列出结果的时候顺便把行号也打出来
echo '3. '
grep -ERn --color=auto 'h[a-z]{4}o' *
