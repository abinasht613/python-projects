mylist1	=	[1,2,3,4]
mylist2	=	[2,4,6]

common	=	[]
for x in mylist1:
	for y in mylist2:
		if x==y:
			common.append(x)
print(common)


print(set(mylist1) & set(mylist2))	#using set [2,4]