#judge the whereabouts

def jw(x, y):
	if x >= 0:
		if y >= 0:
			print"1"
		else:
			print"4"
	if x < 0:
		if y >=0:
			print"2"
		else:
			print"3"
			
x=input()
y=input()
jw(x,y)
