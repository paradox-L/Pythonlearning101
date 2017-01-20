#list comprehension
#str.join(sequence) means connect elements in seq with the str to a new str
me=';'.join([str(i) for i in range(1,101) if i % 30 == 0])
print me
lecture=';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])
print lecture
if me == lecture:
	print True
else:
	print False

#hhh,I'm right!Math is useful:P