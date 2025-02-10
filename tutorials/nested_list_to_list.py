mylist =	[1,[2,[3,[4]],5]]	#[1,2,3,4,5]

newlist	=	[]
def mynested(mylist):
	for x in mylist:
		if isinstance(x,list):
			mynested(x)
		else:
			newlist.append(x)

	return newlist		

print(mynested(mylist))