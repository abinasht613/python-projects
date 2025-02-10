mylist 	=	[2,4,6,8,12,14]

mydiff 	=	min(mylist[x] - mylist[x-1] for x in range(1,len(mylist)))

missing_no	=	None
# print(mydiff)
for x in range(1,len(mylist)):
	if mylist[x]-mylist[x-1]!=mydiff:
		missing_no = mylist[x-1]+mydiff

print(missing_no)