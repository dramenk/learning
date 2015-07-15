#!/usr/bin/python3

# WEB 开发：底层的代码由专门的服务器软件实现，业务Python专注于生成HTML文档
# 这样，学要一个接口：WSGI， web server gateway interface

# application函数就是符合wsgi标准的http处理函数，它接受两个参数：
# environ 一个包含所有http请求header信息的dict对象
# start_response 一个发送http响应header的函数
def application(environ, start_response):
	# 发送header
	start_response('200 OK', [('Content-Type', 'text/html')])
	# 返回body
	print(environ['REQUEST_METHOD'])
	return [b'<h1>Hello, web.</h1>' ]

# 上面的函数必须由wsgi服务器调用，python内置了wsgiref，可供开发测试
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

