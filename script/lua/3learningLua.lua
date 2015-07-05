#!/usr/local/bin/lua

--[[
-- 表达式
--]]--

-- 1. 算术运算符：略
-- 2. 关系运算符：不等号为～=
-- 3. 逻辑运算符：and or not
a = nil; b = 2
print("a(false) and b(2) is ", (a and b)) 	-->a is false, a and b return a 
print("a(false) or b(2) is ", (a or b)) 	-->a is false, a or b return b 

a = 1; b = 2 
print("a(1) and b(2) is ", (a and b))		-->a is true, a and b returns b
print("a(1) or b(2) is ", (a or b))			-->a is true, a and b returns a

-- table在其他语言中称作map映射或者dict字典
-- 下面是table的构造器
theTable = {
	x = "1", 
	y = 2,
	"another field"
}

-- 可以新增filed
theTable["Filed1"] = 60
theTable[2] = 30

-- 通过filed的key获取value
print('theTable["x"] is ' .. theTable["x"])
print('theTable.y is ' .. theTable.y)

-- 如果这个filed没有名字，即没有key，那么第一个这样的值可以通过下标1获取
print('theTable[1] is ' .. theTable[1])

-- 删除
theTable[1]=nil

-- 下标为1的元素已经被删除，下标2的元素也不会被提前，这里元素2依然是30
print('theTable[2] is ' .. theTable[2])

-- 这里的迭代是无序的
for k, v in pairs(theTable) do 
	io.write(k..'\t'..v..'\n')
end
print("===============================================================")

-- table是以对象的方式存储的，变量并不真的持有它们的值，而仅仅是保存了这些对象的引用(reference)。
-- theTable2是theTable1的副本，他们引用的是同一个对象，因此对theTable1所做的更改，同样对theTable2
-- 生效。这类值还包括函数，线程。
theTable1 = {"3", "hello", "2"}
theTable2 = theTable1
for k, v in ipairs(theTable2) do
	print(k, v)
end
print("-----------------------")
table.sort(theTable1)
for k, v in ipairs(theTable2) do
	print(k, v)
end
print("-----------------------")
theTable1[1] = "ke"
for k, v in ipairs(theTable2) do
	print(k, v)
end

