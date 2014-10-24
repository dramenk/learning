# makefile文件的变量，就像C文件中的宏展开
#
OBJS = work/main.o work/hello.o
FINDHPATH = 
CC = gcc $(FINDHPATH)

vod : $(OBJS)
	gcc -o vod $(OBJS)

# include搜索的路径：当前路径;-I路径
include hello.mk

work/main.o : ../main/main.c ../hello/hello.h
	$(CC) -c ../main/main.c -o work/main.o
work/hello.o : ../hello/hello.c ../hello/hello.h
	$(CC) -c ../hello/hello.c -o work/hello.o
clean:
	rm -f work/*.o vod
