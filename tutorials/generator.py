def countotN(n):
	count=1
	while count<=n:
		yield count
		count+=1	

def normalFuntion(n):
	count =1
	mylist=[]
	while count<=n:
		mylist.append(count)
		count+=1
	return mylist	

for x in countotN(5):
	print(x)

# for x in normalFuntion(5):
# 	print(x)