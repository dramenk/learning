#!/usr/local/bin/lua

--[[
-- 函数 
--]]--

-- 1. 多值返回，多退少补nil
function A()
	return 1, 2, 3, 4
end

function B()
	return 1, 2
end

a, b = A()
print(a, b)
a, b, c = B()
print(a, b, c)

-- 加（）强制返回1个值
a, b, c =(B())
print(a, b, c)

a = {1, 2, 3, 4}
print(a)
print(table.unpack(a))

-- 可变参数
function myPrint(...)
	for k, v in ipairs{...} do
		io.write(tostring(v)..'\t')
	end
	io.write("\n")
end
myPrint(4, 5, 6)

-- 命名参数的实现:通过table的构造
function rename(arg)
	return os.rename(arg.old, arg.new)
end

rename{old="temp.lua", new="temp1.lua"}

