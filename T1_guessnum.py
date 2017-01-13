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

    if answer>num:
        print"too big"
    if answer<num:
        print"too small"
    if answer==num:
        print"Bingo!"
        bingo=True

