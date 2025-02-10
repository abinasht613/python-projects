from collections import Counter

mystring	=	"Abinash"
mystring	=	mystring.lower()
print(mystring)
mycounter =	Counter(mystring)
print(mycounter)
for x in mycounter.keys():
	if mycounter[x]==1:
		print(f"first non repeating is {x}")
		break
