#play soccer with computer

from random import choice

score_you=0
score_com=0

direction=["left", "center", "right"]

def compete(kicker,kicker_score,saver,saver_score):
	if kicker != saver:
		print"Goal!!"
		kicker_score += 1
	else:
		print"Oops..."
		saver_score +=1

for i in range(5):
	print"======Round%d You kick the ball======"%(i+1)

	you=raw_input("Select from left, center or right:   ")
	print"You kick to %s"%you
	computer=choice(direction)
	print"Computer save the %s"%computer

	compete(you,score_you,computer,score_com)
	print"The Score now:%d(you):%d(computer)"%(score_you, score_com)

	print"======Round%d You save the ball======"%(i+1)

	you=raw_input("Select from left, center or right:   ")
	print"You save the %s"%you
	computer=choice(direction)
	print"Computer kick to %s"%computer
	compete(computer,score_com,you,score_you)

	print"The Score now:%d(you):%d(computer)"%(score_you, score_com)
