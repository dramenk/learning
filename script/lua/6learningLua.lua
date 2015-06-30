#!/usr/local/bin/lua

--[[
-- 函数 
--]]--

-- 1. 函数也是第一类值
a = {p = print}
a.p("函数也是第一类值。")

-- 以函数作为入参的函数称为高级函数
network = {name = "leshi"}
table.sort(network, function(a, b)
	return (a.name > b.name)
end)

-- 2. 函数的词法定界
-- 被嵌套的函数可以访问其外部函数中的变量
-- 闭包
function newCounter()
	local i = 0
	return function()
		i = i + 1
		return i
	end
end

c1 = newCounter()
print(c1()) -->1
print(c1()) -->2

c2 = newCounter()
print(c2()) -->1
print(c1()) -->3
