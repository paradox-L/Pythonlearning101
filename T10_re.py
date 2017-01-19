#re is a module in Python
import re

text = "site sea sue sweet see case sse ssee loses"

#r : raw,not to transfer meaning of str
#. : represent any character except \n
#* : the character in front of * plus n times(n can be zero)
#\S : represent any not blank character
#? : transfer greedy mode into lazy mode
m=re.findall(r'\bs\S*?e\b',text)
if m:
	print m
else:
	print"Not matched"


#suppose there is a file named number.txt
import re

f = open(number.txt)
line = f.readlines()
f.close()

pnumber = re.findall(r'\b1\d{10}\b',line)

#for further learning:
#正则表达式30分钟入门教程 http://deerchao.net/tutorials/regex/regex.htm#regexoptions