#!/usr/local/bin/lua

--[[
--协同程序
--比较类似与线程：有独立的堆栈，局部变量和指令指针，同其他协程共享全局变量
--不同之处：在多处理器场景下，能够同时运行多个线程，但是协程在同一时刻只会
--运行一个，是通过串行写作来完成某一功能。
--]]

--创建协程，入参为函数地址，返回thread类型值
co = coroutine.create(function ()
	print("hi")
end)

print(co) 					-->打印返回值
print(coroutine.status(co)) -->初始状态一定是挂起状态
coroutine.resume(co) 		-->进入运行状态，执行协同体函数

--协程的独特之处在于运行过程中的挂起
co = coroutine.create(
function ()
	for i = 1, 2 do
		print("co", i)
		coroutine.yield()
	end
end)
print(coroutine.resume(co)) -->执行协同体，并打印执行成功是resume的返回值true
print(coroutine.status(co))
coroutine.resume(co)
print(coroutine.status(co))
coroutine.resume(co)		-->协同体结束，这里不会打印任何值
print(coroutine.status(co)) -->dead状态
print(coroutine.resume(co)) -->这里的错误是返回的，不会抛出，因为rusume运行在保护模式下

--resume yield可以传递入参和返回值
co = coroutine.create(function(a, b)
	print("co", a, b)
	coroutine.yield(a+b, a-b)
	return "hello"
end)
print(coroutine.resume(co, 1, 2))  -->打印结果true，返回值3, -1
print(coroutine.resume(co, 3, 4))  -->打印结果true，最后的return值hello也会返回给resume而被打印

--[[
利用协程可以写一个迭代器，迭代器是一个函数，每次调用返回对应的值。
--]]
function printResult (a)
	for i,v in ipairs(a) do
		io.write(v, " ")
	end
	io.write("\n")
end

function permgen (a, n)
	if n == 0 then
		coroutine.yield(a)
	else
		for i=1,n do
			-- put i-th element as the last one
			a[n], a[i] = a[i], a[n]
			-- generate all permutations of the other elements
			permgen(a, n - 1)
			-- restore i-th element
			a[n], a[i] = a[i], a[n]
		end
	end
end

function perm (a)
	local n = #a
	local co = coroutine.create(function () permgen(a, n) end)
	return function ()
		-- iterator -->迭代器是一个函数，每一回被调用都会返回不同的对应的值，这个return不能省略，因为
		-- 如果直接return res，res却是一个table，table当然作不了迭代器。调用迭代器函数返回table才对。
		local code, res = coroutine.resume(co)
		return res
	end
end
for p in perm ({1,2,3,4}) do
	printResult(p)
end


--[[
Lua 中的协同是一协作的多线程,每一个协同等同于一个线程,yield-resume 可以实现在线程中切换。
然而与真正的多线程不同的是,协同是非抢占式的。当一个协同正在运行时,不能在外部终止他。只能
通过显示的调用 yield 挂起他的执行。
--]]
