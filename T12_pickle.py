#pickle to order data
#picke.dump(variable,filename)

import pickle

f=open('test.txt')
line = pickle.load(f)
print line
f.close()