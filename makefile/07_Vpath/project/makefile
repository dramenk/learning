# makefile文件的变量，就像C文件中的宏展开
#
#

OBJS = work/main.o work/hello.o

# makefile的vpath关键字可以指定 目标文件 和 依赖文件 的搜索范围
# 下面的三行指示如果当前路径找不到.o的目标或者依赖文件，那么就去
# work目录下寻找.c文件还可去../main以及../hello目录下寻找
vpath %.o work
vpath %.c ../main:../hello
vpath %.h ../hello

vod : main.o hello.o
	gcc -o vod $(OBJS)

# .o 和 .h不在一个目录下貌似自动推导的功能还是不可用，main.o和
# 的依赖关系建立不起来。这可能也就是ATS编译工程修改.c文件编译的
# 时候为什么要删除对应.o文件的原因
# main.o : hello.h
main.o : main.c hello.h 
	gcc -c ../main/main.c -I ../hello/ -o work/main.o

hello.o : hello.c hello.h
	gcc -c ../hello/hello.c -o work/hello.o

clean:
# 通常，make会把要执行的命令行在命令执行前输出倒屏幕上，当我们用
# @ 字符放在命令行前，那么这个命令将不被make显示出来
# echo 正在编译模块...
# 将会显示成：
# echo 正在编译模块...
# 正在编译模块...
# 另外，如果命令执行出错，命令前面又没有"-"，那么make会终止当前规则
# 的执行！
	@rm -f work/*.o vod
	@echo clean! 
