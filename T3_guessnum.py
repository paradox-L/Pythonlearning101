#guess number by function

from random import randint

num=randint(1,100)
bingo=False

def compare(answer, num):
	if answer > num:
		print"too big"
		return False
	elif answer < num:
		print"too small"
		return False
	else:
		print"bingo!"
		return True

while bingo==False:
	answer = input()
	bingo = compare(answer,num)