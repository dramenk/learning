#!/usr/bin/python3

import os
import multiprocessing
import subprocess

# 多任务的实现有3种方式：
# 多进程模式；
# 多线程模式；
# 多进程+多线程模式。
# 一个进程至少有一个线程。

# python的os模块封装了Unix的fork()系统调用，可以实现多进程
#print('Process (%s) start...' % os.getpid())
#pid = os.fork()
#if pid == 0:
#	print('I am child process(%s) and my parent is %s.' % (os.getpid(), os.getppid()))
#else:
#	print('I am parent process(%s)', os.getpid())

# 由于window没有fork系统调用，python提供了multiprocessing模块支持跨平台的多进程
# multiprocessing提供了Process类来代表一个进程对象
def run_proc(name):
	print('Run child process %s(%s)...' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s' % os.getpid())
	p = multiprocessing.Process(target=run_proc, args=('hello',))
	print('Child will start.')
	p.start()						# 用start()方法启动一个子进程
	p.join()						# 父进程等待子进程执行完毕
	print('Child process end.')

# 另外，可以通过进程池multiprocessing.Pool对象批量创建进程(略)

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)