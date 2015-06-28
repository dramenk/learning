#!/usr/bin/lua

-- function
function fib(n)
	if n > 2 then
		return fib(n-1)+fib(n-2)
	else
		return 1
	end
end

for i=1,10 do
	print(fib(i))
end
