#!/usr/bin/python3

import os, sys, time
import multiprocessing

# 多任务的实现有3种方式：
# 多进程模式；
# 多线程模式；
# 多进程+多线程模式。
# 一个进程至少有一个线程。

#### 多进程 ####
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
	print('Run child process %s(%s) ' % (name, os.getpid()), end='')
	for i in range(10):	
		time.sleep(0.5)
		print('.', end='')
		sys.stdout.flush()
	print('')

if __name__ == '__main__':
	print('Parent process %s' % os.getpid())
	p = multiprocessing.Process(target=run_proc, args=('hello',))
	print('Child will start.')
	p.start()						# 用start()方法启动一个子进程
	p.join()						# 父进程等待子进程p执行完毕
	print('Child process end.')

# 另外，可以通过进程池multiprocessing.Pool对象批量创建进程(略)

# 子进程还可以是外部进程
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# 采用Queue机制进行进程间通信
def write(q):
	print('Process to write: %s' % os.getpid())
	time.sleep(0.5)
	for value in 'ABC':
		print('Put %s in queue.' % value)
		q.put(value)
		time.sleep(1)

def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	q 	= multiprocessing.Queue()
	pw 	= multiprocessing.Process(target = write, args = (q,))
	pr	= multiprocessing.Process(target = read,  args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()

#### 多线程 ####
import threading

def loop():
	# threading.current_thread()返回当前线程的实例	
	print('thread %s is running ...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n += 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(0.5)
	print('thread %s end.' % threading.current_thread().name)

if __name__ == '__main__':
	# 主线程实例的名字叫做MainThread
	print('thread %s is running ...' % threading.current_thread().name)
	# 主线程可以启动子线程，子线程的名字由threading.Thread()方法的name参数传入
	t = threading.Thread(target = loop, name = 'LoopThread')
	t.start()
	t.join()
	print('thread %s end.' % threading.current_thread().name)

# 线程锁,线程中修改局部变量需要注意是否需要加锁
balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance -= n
	balance += n

def run_thread(n):
	for i in range(1000000):
		lock.acquire()
		# 为了防止在change_it中出现异常导致后续代码不能执行，可以使用try...finally...
		# 保证锁的释放，以免其他线程一直在等待该锁，成为死线程。
		try:
			change_it(n)
		finally:
			lock.release()

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 多进程稳定性高一些，效率稍低；多线程稳定性差，效率稍高。
# 另外，多任务也需要注意任务切换的开销；任务一旦过多，就会造成哪个任务也做不好。

