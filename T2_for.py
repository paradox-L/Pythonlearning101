# -*-coding:utf-8-*-

#add nums from 1 to 100
sum = 0
#这里n放在循环句块外是因为你希望n在while循环里一直累加
#不同于T1每循环一次都给n重新赋值
n=0
while n <= 100:
	n=n + 1
	sum=sum + n

print sum

#nesting for circulation
#draw a triangle
for i in range(0,5):
	for j in range(0,i+1):
		print"*",
	print
	