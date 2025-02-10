class myaccessmodifier:

	def __init__(self,age,salary,name):
		self.__salary	=	salary
		self._age		=	age
		self.name		=	name

	def mysalary(self):
		return self.__salary

	def myage(self):
		return self._age

	def myname(self):
		return self.name

	def addsalary(self,salary):
		self.__salary	=	salary

myobj	=	myaccessmodifier(30,100000,'Abinash')
print(myobj.mysalary())
print(myobj.name)
print(myobj._age)
# print(myobj.__salary)
myobj.addsalary(90000)
print(myobj.mysalary())
