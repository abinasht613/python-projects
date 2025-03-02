from abc import ABC, abstractmethod


class Myabstract(ABC):
	@abstractmethod
	def myAbstractMethod(self):
		pass

	def myConcreteMethodAbstract(self):
		print("print from Myabstract myConcreteMethod")

class MyConcreteClass(Myabstract):
	def myConcreteMethod(self):
		print("print from MyConcreteClass myConcreteMethod")

	def myAbstractMethod(self):
		print("print from MyConcreteClass myAbstractMethod")

	def myConcreteMethodAbstract(self):			#override
		print("print from MyConcreteClass myConcreteMethod")


myobj = MyConcreteClass()
myobj.myAbstractMethod()
myobj.myConcreteMethod()
myobj.myConcreteMethodAbstract()

