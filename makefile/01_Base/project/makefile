vod : work/main.o work/hello.o
	gcc -o vod work/main.o work/hello.o
work/main.o : ../main/main.c ../hello/hello.h
	gcc -c ../main/main.c -I ../hello/ -o work/main.o
work/hello.o : ../hello/hello.c ../hello/hello.h
	gcc -c ../hello/hello.c -o work/hello.o
clean:
	rm -f work/*.o vod
