# -*-coding:utf-8-*-
from random import randint

name=raw_input('What is your nickname?')
try:
    #read history score from file
    f=open('game.txt')
    #each line represents a user's data
    lines=f.readlines()
    f.close()
except:
    print'You need to create "game.txt"with 1st line"0 0 0"under the dir'

#create a dictionary of user:data
scores={}
for line in lines:
    #part data into 3 str in list"data"
    data=line.split()
    #define key-name:value-score
    scores[data[0]]=data[1:]
#checkout whether user is in dic already
user=scores.get(name)
if user==None:
    user=[0, 0, 0]
#count
start_times=int(user[0])
min_times=int(user[1])
total_times=int(user[2])
if start_times>0:
    avg_times=float(total_times)/start_times
else:
    avg_times=0

print"%s has played %dround(s).Minium use %d.Average use %.2f"%(name,start_times,min_times,avg_times)

num=randint(1, 100)
print"Guess what I am thinking?"
bingo=False
times=0

while bingo==False:
    times += 1
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
#save the user's score
if start_times==0 or times<min_times:
    min_times=times
total_times += times
start_times += 1

#mode'w'will cover record before
#So update the dic"scores" then 'w' all anew
#username:start_times,min_times,total_times
scores[name]=[str(start_times), str(min_times), str(total_times)]

#fomatting data
result=''
for n in scores:
    putin=n+' '+' '.join(scores[n])+'\n'
result += putin

f = open('game.txt','w')
f.write(result)
f.close()