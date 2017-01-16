# -*-coding:utf-8-*-
from random import randint

num=randint(1, 100)

print"Guess what I am thinking?"
bingo=False

while bingo==False:
    #给answer赋值的式子要写在循环语句块内
    #这样每循环一次都会给answer重新赋值
    #否则answer值被固定while陷入死循环
    answer=input()

    if answer<0:
        print"Exit game"
        break

    if answer>num:
        print"%d is too big"%answer
    if answer<num:
        print"%d is too small"%answer
    if answer==num:
        print"Bingo!%d is the answer"%answer
        bingo=True