oldList =	[1,2,3,5,7,8,9,11,12,13]				#list comprehension
newList	=	[x**2 for x in oldList if x%2==0]
print(f"{newList}")



mydict = {								#dictionary comprehension
		'a':1, 'b':2,'c':3
}

mydict_new	=	{value:x for x,value in mydict.items()}
print(mydict_new)

													
keys	=	['a','b','c','d']
values	=	[1,2,3,4]
mydictCom	=	{k:v for (k,v) in zip(keys,values)}
print(mydictCom)
evenSquare	=	{x:x**2 for x in values if x%2==0}
print(evenSquare)