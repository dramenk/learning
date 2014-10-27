# makefile文件的变量，就像C文件中的宏展开
#
# 注意：变量是大小写敏感的
#
# 还有一种变量定义的方式是“:=”，这个和“=”是有一些不同的=是可以全文refer to的，
# 而:=只能refer to语句之前的，若OBJS := MAINOBJ HELLOOBJ，那么OBJS展开为：
# work/main.o
# OBJS ?= work/main.o work/hello.o的意思是OBJS之前定义过么，定义过就算了，
# 没定义过就让它等于work/....吧
MAINOBJ = work/main.o
OBJS = MAINOBJ HELLOOBJ
HELLOOBJ = work/hello.o
vod : $(OBJS)
	gcc -o vod $(OBJS)
work/main.o : ../main/main.c ../hello/hello.h
	gcc -c ../main/main.c -I ../hello/ -o work/main.o
work/hello.o : ../hello/hello.c ../hello/hello.h
	gcc -c ../hello/hello.c -o work/hello.o
clean:
	rm -f work/*.o vod
# 系统变量MAKELEVEL：如果makefile嵌套调用了，那么这个变量会记录下调用的层数
# 
# 变量的高级用法：
# foo := main.o hello.o
# bar := $(foo:.o=.c) # bar的值是main.c hello.c
# bar := ${foo:.o=.c}
# bar := $(foo:%.o=%.c) # 静态模式
# 
# 嵌套调用makefile可以通过make命令行或者export成环境变量传递变量
#
# target-specific-varible:如$<，规则型变量，作用范围仅仅在本条规则以及连带
# 的规则中。
#
# pattern-specific varible如:
# %.o:CFLAGS=-O,给所有以.o结尾的目标定义目标变量CFLAGS.
