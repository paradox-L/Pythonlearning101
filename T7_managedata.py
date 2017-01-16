# -*- coding: utf-8 -*-

try:
    f=file('data.txt')
    #把每一行拆成列表里的字符串单位
    lines=f.readlines()
    print"File opened"
    f.close()
except:
    print"No such file found"
print"Inspect finished"


results=[]
for line in lines:
    #把一行里的每个词组按空格拆成单位
    data=line.split()
    sum=0
    for score in data[1:]:
        #略过低于60分的成绩
        if int(score)<60:
            continue
        sum += int(score)
    result="%s\t:%d\n"%(data[0],sum)
    
    results.append(result)

output=open('finals.txt','w')
output.writelines(results)
output.close()