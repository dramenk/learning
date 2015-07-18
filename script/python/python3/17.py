#!/usr/bin/env python3

# 异步IO
# 由于CPU的速度远大于磁盘网络的IO，因此一般程序遇到IO操作时，需要等待IO操作完成（同步IO）
# 因为IO操作阻塞了当前线程，导致其他代码无法执行，所以常用多线程或进程来并发执行代码，为
# 多个用户服务。
# 但是系统不能无限制增加线程，切换线程开销也很大，线程过多会导致系统性能严重下降。
# 还有另一种方法能够解决IO问题：异步IO
# 即，执行IO操作时，通过发出指示，而不原地等待结果；当IO结果返回，再由CPU进行处理。
# 异步IO需要一个消息循环，在消息循环中，主线程不停的读取-处理消息
# 比如桌面GUI：键盘和鼠标等消息被发送到GUI程序的消息队列中，然后由GUI主线程不停的处理。这
# 中模型需要一个条件：即单条消息的处理总是很快的，否则会影响到线程无法及时处理消息队列中
# 的其他消息，使得程序看上去像停止响应。

# 协程
# 函数内部能够中断，转而执行其他函数，这种切换不采用传统的调用。相较于多线程，切换由程序
# 自身控制，这种切换更高级而非像线程切换由系统控制，由于受程序自身控制也不需要线程锁；不
# 存在线程切换的开销。
# 由于协程实际只有一个线程，可以通过多进程+协程充分利用多核CPU
# 下面是说明协程的经典的生产者-消费者模型：
def consumer():
	r = ''
	while True:
		n = yield r									# consumer通过yield拿到东西n，后通过yield把结果r传回
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 OK'
		
def produce(c):
	c.send(None)									# 启动生成器
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)								# 东西n已经生成，切换到consumer
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()										# produce决定不生产了，通过c.close()关闭consumer，整个过程结束
		
c = consumer()
produce(c)

# asyncio是3.4内置对异步IO支持的标准库
import asyncio
import threading

@asyncio.coroutine
def hello():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(2)						# 走到这里，中断，执行任务中的其他coroutine
	print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]							# 两条打印，等2秒，再两条again打印
loop.run_until_complete(asyncio.wait(tasks))

@asyncio.coroutine
def wget(host):
	print('wget %s...' % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	# Ignore the body, close the socket
	writer.close()
		
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

