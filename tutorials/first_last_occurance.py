# Write a program to find first and last occurence of given numbers
# input1: (1,3,3,3,4,5,6,7,7,7,7)
# input2: 3, 7
# output : first occurence of 3 and last occurence of 7 [1,10]
from collections import Counter


output =	[]
def myfun(s1,s2):
	for j,y in enumerate(s2):
		myCount=1
		myListCounter	=	Counter(s1)
		# print(myListCounter[y])
		for i,x in enumerate(s1):
			if x==y:
				if j==0:
					output.append(i)
					break
				if j==1:
					if myCount==myListCounter[y]:
						# print('a')
						output.append(i)	
					else:
						# print(f"b: {myCount}")
						myCount+=1
	return output	


myinput	=	[1,3,3,3,4,5,6,7,7,7,7]
mycheck	=	[3,7]
test = myfun(myinput,mycheck)

print(test)			# [1,10]
