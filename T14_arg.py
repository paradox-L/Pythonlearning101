# -*-coding:utf-8-*-
#arg
def func(arg1=1, arg2=2, arg3=3):
	print arg1,arg2,arg3

print func(4,5,6)
print func(4,5)
print func(4)
print func(arg2=8)
print func(11,arg3=12)

def calcsum(*arg):
	sum=0
	for i in arg:
		print i
		sum += i
	print sum

calcsum(1,2,3)
calcsum(123,321)
calcsum()

print"Comprehensive using"
#notice the arg's order of different type
def superfunc(x,y=2,*a,**b):
	print x,y,a,b

func(1)
func(1,2)
func(1,2,3)
func(1,2,3,4)
func(x=1)
func(x=1,y=1)
func(x=1,y=1,a=1)
func(x=1,y=1,a=1,b=1)
func(1,y=1)
func(1,2,3,4,a=1)
func(1,2,3,4,k=1,t=2,o=3)

#the process
'''
1.按顺序把无指定参数的实参赋值给形参；
2.把指定参数名称(arg=v)的实参赋值给对应的形参；
3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
4.将多余的指定(a=xxx)参数名的实参打包成一个 dict 传递给字典参数(**kargs)
'''