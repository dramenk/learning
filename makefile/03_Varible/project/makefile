# makefile文件的变量，就像C文件中的宏展开
#
# 注意：变量是大小写敏感的
#
# 还有一种变量定义的方式是“:=”，这个和“=”是有一些不同的
# =是可以全文refer to的，而:=只能refer to语句之前的
# 若OBJS := MAINOBJ HELLOOBJ，那么OBJS展开为：
# work/main.o
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
