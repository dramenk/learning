# from multiprocessing import Process
# import os


# def runprocessing(name):
# 	print 'process(%d): %s' % (os.getpid(), name)

# f = os.fork()

# if f > 0:
# 	print 'This is parent, pid is %d, whose child is %d' % (os.getpid(), f)
# else:
# 	print 'This is child, pid is %d, whose parent is %d' % (os.getpid(), os.getppid())

# p = Process(target=runprocessing, args=('test',))
# p.start()
# p.join()

# print 'Processing end.'

#####################################################################

# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.' % (name, (end - start))

# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'

#####################################################################

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
