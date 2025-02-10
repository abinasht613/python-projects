class myclass:
	myCounter=0

	@classmethod
	def myclassmethod(cls):
		cls.myCounter+=1
		return cls.myCounter

	@staticmethod
	def sum(a,b):
		return a+b

	def __init__(self,a,b):
		self.a=a
		self.b=b

	def myprint(self):
		return self.a+self.b		

print(myclass.sum(2,4))
print(myclass.myclassmethod())
print(myclass.myclassmethod())
 
myobj	=	myclass(5,5)
print(myobj.myprint())