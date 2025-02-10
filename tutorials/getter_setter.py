class Myclass:

	def __init__(self,age):
		self.__age=age
	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self,age):
		if age>0:
			self.__age=age
		else:
			self.__age=0


myobj = Myclass(30)
print(myobj.age)
myobj.age = 31
print(myobj.age)
