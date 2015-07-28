#!/usr/bin/expect

# expect 自动交互 

# spawn, expect 需要另外安装
spawn ./07_read.sh
expect "Please input the first name:"
send "ke\n"
expect "Please input the last name:"
send "longwen\n"
expect "3 characters will be received:"
send "abc"
expect "Enter your password:"
send "king\n"
expect eof
