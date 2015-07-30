#!/usr/local/bin/lua

--[[
-- 基本语法
--]]--

-- 1. 赋值，支持多值赋值
a, b, c = 1
print(a, b, c) ---> 1, nil, nil

-- 2. 局部变量的作用范围：只在声明其的代码块内有效
-- 代码块： 一个控制结构内（条件+循环）； 一个函数体； 一个chunk
x = 10

local i = 1 -->local to the chunk
while i <= x do
	local x = i * 2 --> local to the while body
	print(x) --> 2, 4, 6, 8...
	i =i + 1
end

function printx()
	local x = 'this is local to function.'
	print(x)
end
printx()

-- 3. break return 只能出现在代码块的末尾
return "break return" 
