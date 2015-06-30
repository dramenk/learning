#!/usr/local/bin/lua

--[[
-- 迭代器 范性for 
--]]--

-- 常常使用函数来表示迭代器，每次调用这个函数都会返回集合的下一个元素。
--
-- 迭代器可以用闭包实现
--
-- 闭包是一个内部函数，它可以访问一个或者多个外部函数的外部的局部变量，
-- 每次闭包的成功调用，这些外部函数的外部局部变量都保存他们的值。
-- 一个典型的闭包结构包含两个函数：一个是闭包自己；另一个是工厂。

-- 一个list的迭代器描述
function list_iter(t)
	local i = 0
	local n = #t
	return function()
		i = i + 1
		if i <= n then return t[i] end
	end
end

-- 迭代器的使用
t = { 10, 20, 30 }
iter = list_iter(t) -->创建迭代器
while true do
	local element = iter() -->调用迭代器
	if element == nil then break end
	print(element)
end

-- 迭代器应用于范性for
for element in list_iter(t) do
	print(element)
end

print("--------------------------------------------------------------")
-- 范性for的实例
for element in ipairs(t) do
	print(element, ipairs(t))
end

-- 这里的ipairs和上面的迭代器不是一回事
print(list_iter(t))
print(ipairs(t))

print("--------------------------------------------------------------")

-- 范性for的原理
functionLoop, status, control = ipairs(t)
while true do
	control = functionLoop(status, control)
	if control == nil then break end
	print(status[control])
end



