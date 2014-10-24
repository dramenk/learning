
# 这个伪目标all可以使得一个make命令，一口气生成vod1和vod2两个程序文件
all : vod1 vod2

#-----------------------------------------------------------
vod1 : work/main.o work/hello.o
	gcc -o vod1 work/main.o work/hello.o
vod2 : work/main.o work/hello.o
	gcc -o vod2 work/main.o work/hello.o

#-----------------------------------------------------------
work/main.o : ../main/main.c ../hello/hello.h
	gcc -c ../main/main.c -I ../hello/ -o work/main.o
work/hello.o : ../hello/hello.c ../hello/hello.h
	gcc -c ../hello/hello.c -o work/hello.o

#-----------------------------------------------------------
clean:
	rm -f work/*.o vod
