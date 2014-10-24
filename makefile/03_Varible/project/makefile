# makefile文件的变量，就像C文件中的宏展开
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
