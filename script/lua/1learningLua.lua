#!/usr/bin/lua

-- This is LINE comment.
--[[ 
This is BLOCK 
comment
--]]
print "Hello lua."

-- string variable
str = 'alo\n123"'
print(str) -- NOT print str, diff from Python

-- while loop, do...end is just like {...} is C language
sum, i = 0, 0
while i <= 50 do
	sum = sum + i
	i = i + 1
end
print("WHILE LOOP: sum of 0 to 50 is", sum)

-- for loop
sum = 0
for i = 0, 50 do
	sum  = sum + i
end
print("FOR LOOP: sum of 0 to 50 is", sum)

-- if and else, 不像shell和Python，没有符号：或者[],目前使用到符号的仅有运算符
-- 和函数调用时的小括号
-- if,then
-- while,do
-- 后面都带有end
age, sex = 45, "Male"
if age == 40 and sex =="Male" then
    print("男人四十一枝花")
elseif age > 60 and sex ~="Female" then
    print("old man without country!")
elseif age < 20 then
    io.write("too young, too naive!\n")
else
	print "Print your age:"
    local age = io.read()
    print("Your age is "..age)
end
