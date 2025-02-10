def myDec(fun):
	def wrapper(a,b):
		return (a+b)**2
	return wrapper



@myDec
def sum(a,b):
	return a+b

print(sum(2,4))