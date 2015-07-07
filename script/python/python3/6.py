#!/usr/bin/python3

from PIL import Image
import sys

# 安装第三方模块,pypi网站
# pip命令，比如：pip install pil
# pil是一个图形处理库，pil只支持到python2.7，基于pil的pillow可以支持python3
# pip install pil可能会：
# Could not find any downloads that satisfy the requirement PIL
# Some externally hosted files were ignored (use --allow-external PIL to allow).
# 这是由于某些版本(1.5)的pip的一些安全增强特性所致，当安装pil时，安装文件实际来
# 自于effbot.org, pypi没有校验和保证安全，需要增加 --allow-external
# pip install PIL --allow-external pil --allow-unverified
# 建议使用pillow库代替pil库

# 我在安装pillow库时：pip3 install pillow, 编译提示找不到Python.h
# 通过安装python3-devel包解决了这个问题

im = Image.open("test.png")
print("width =", im.width)
print("height =", im.height)
print("mode =", im.mode)
print("size =", im.size)
print("format =", im.format)
im.thumbnail((200, 100))
#im.save('thumb.jpg', 'JPEG')

# 试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错
# 搜索路径存放在sys模块的path变量中,路径可以通过sys.path或者环境变量PYTHONPATH更改。
print(sys.path)
