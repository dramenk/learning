#!/usr/bin/env python3
from flask import Flask, request, render_template

# MVC, Model-View-Controller
# Model: 	传递给view的dict
# View：	html页面，放置到templates目录下
# Controller: python逻辑

# flask默认采用使用{% ... %}和{{xxx}}的jinja2模板
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == 'password':
		# 函数的关键字参数
		return render_template('signin_ok.html', username = username)
	else:
		return render_template('form.html', message = 'Bad username or password.', username = username)

if __name__ == '__main__':
	app.run()
