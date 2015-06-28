#!/usr/local/bin/lua

print("This script is learning for table in LUA.")

-- table在其他语言中称作map映射或者dict字典
theTable = {
	x = "1", 
	y = 2,
	"another field"
}

-- 可以新增filed
theTable["newFiled1"] = 60
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
