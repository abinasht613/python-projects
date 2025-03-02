# mylist=[[[1,2],3],4]


# resultList=[]
# def mynested(mylist):
# 	for x in mylist:
# 		if isinstance(x,list):
# 			mynested(x)
# 		else:
# 			resultList.append(x)
# 	return resultList

# print(mynested(mylist))


# mydict = {
# 		'a':1, 'b':2,'c':3
# }

# mydict_new	=	{value:x for x,value in mydict.items()}
# print(mydict_new)
# print(mydict.values)

# a:int = 2
# b:int = 3

# mysum:int= a+b 
# print(mysum)

# mylist: list[int] = [1, 2, 3, 4, 5]

# mysum2:int = sum(mylist)


def mysum(a:int,b:int) -> int:
	return a+b

a:int = 2
b:int = 3

print(mysum(a,b))
