#open file;when pull out content from file remember .read()
#file() equals to open()

f=file('gitcheat.txt')
data=f.read()
print data
f.close()
#write into file
#mode:'r','w','a'
line="I will be in a file.\nSo cool!"
output=open('output.txt','w')
output.write(line)
#append data from other file
a=open('readme.txt')
addition=a.read()
new=open('output.txt','a')
output.write(addition)
a.close()
new.close()
#input content from cmd
b=open('readme.txt','a')
interaction=raw_input('What you type now will be saved in file:\n')
b.write(interaction)
b.close()
