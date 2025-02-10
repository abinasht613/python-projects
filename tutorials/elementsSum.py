mylist  =	[1,3,6,8,4,2]  # sum 10 (6+4),(8+2)
target=	10

targetList	=	[]
for x in mylist:
	mydiff	=	target - x
	if mydiff in mylist:
		targetList.append({x,mydiff})

print(targetList)