# import sys;sys.path.append('/usr/lib/python2.7/site-packages/mysql_connector_python-2.0.3-py2.7.egg')
# import mysql.connector

# conn = mysql.connector.connect(user='root', password='kingdom', database='test', use_unicode=True)
# cursor = conn.cursor()
# try:
# 	cursor.execute('create table test_table (col1 int not null, col2 int not null)')
# 	for n in range(10):
# 		cursor.execute('insert into test_table(col1, col2) values(%s, %s)', [n, n*n])
# 	print cursor.rowcount
# 	cursor.execute('select * from test_table')
# 	values = cursor.fetchall()
# 	for n in values:
# 		print n
# except mysql.connector.errors.ProgrammingError, e:
# 	print e
# finally:	
# 	cursor.execute('drop table test_table')
# 	cursor.close()

# import os

# f = open('/home/kelongwen/Project/annotated_redis_source/src/redis.h', 'r')
# for n in f.readlines():
# 	print n.decode('gbk'),
# f.close()

for n in range(200):
	print "%d & 6 = %d" % (n, n&7)
