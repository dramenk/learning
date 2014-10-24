# makefile文件的变量，就像C文件中的宏展开
# 自动推导功能和收拢的功能由于这个例子是分模块文件夹的，
# 目前还不知道这种情况下怎么弄，所以……这个例子演示不了
#
OBJS = work/main.o work/hello.o
vod : $(OBJS)
	gcc -o vod $(OBJS)
work/main.o : ../main/main.c ../hello/hello.h
	gcc -c ../main/main.c -I ../hello/ -o work/main.o
work/hello.o : ../hello/hello.c ../hello/hello.h
	gcc -c ../hello/hello.c -o work/hello.o
clean:
	rm -f work/*.o vod
