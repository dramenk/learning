# makefile文件的变量，就像C文件中的宏展开
#
OBJS = work/main.o work/hello.o
FINDHPATH += 
# 看main函数代码，下面一行表示#define ATS_VCU
CFLAGS += -DATS_VCU
CC = gcc $(FINDHPATH) $(CFLAGS)

vod : $(OBJS)
	gcc -o vod $(OBJS)

# include
include hello.mk

work/main.o : ../main/main.c ../hello/hello.h
	$(CC) -c ../main/main.c -o work/main.o
work/hello.o : ../hello/hello.c ../hello/hello.h
	$(CC) -c ../hello/hello.c -o work/hello.o
clean:
	rm -f work/*.o vod
