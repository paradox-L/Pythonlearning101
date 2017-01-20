#lambda grammar format:lambda arg*:expression
sum = lambda a, b, c : a + b + c
print sum(1,2,3)

def fn(x):
	return lambda y:x + y

newfunc=fn(1)
print newfunc(2)