#!/bin/bash

# find查找

# 这里仅仅举例，详细参数通过man find查找

# 列出当前目录和子目录所有的文件: find root_path
# -print 表示输出定界符为\n
# -print0 表示输出定界符为\0
echo "1. find . -print0"
find . -print0
echo ""

# 按照文件名查找：-name -iname(忽略大小写)
echo '2. find . -iname "*Fi*"'
find . -iname "*Fi*"

# 否定参数
echo '3. find . ! -iname "*.sh"'
find . ! -iname "*.sh"

# 文件类型：-type （d：目录；f：文件；l：符号连接）
# 要文件不要目录
echo '4. find . -type f ! -iname "*.sh"'
find . -type f ! -iname "*.sh"

# 目录深度: -maxdepth -mindepth
echo '5. find . -maxdepth 1 ! -iname "*.sh"'
find . -maxdepth 1 ! -iname "*.sh"

# 文件时间：mtime atime ctime(change time，元数据被更改)
# 最近三天被修改过的文件
echo '6. find . -type f -mtime -3'
find . -type f -mtime -3

# 文件大小，大于512字节的文件
echo '7. find . -type f -size +1'
find . -type f -size +1

# 文件权限: -perm
echo '8. find . -type f -iname "*.sh" ! -perm 775 -print'
find . -type f -iname "*.sh" ! -perm 775 -print0;echo
# 批量改权限
chmod 755 `find . -type f -iname "*.sh" ! -perm 755` 2> /dev/null

# 文件所有者
echo '9. find . -type f -user root' 
find . -type f -user root
