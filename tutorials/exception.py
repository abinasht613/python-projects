class MyException(Exception):
	def __init__(self,age,min_age=18):
		super().__init__(f"{age} is less then {min_age}")

try:
		age=16
		if age<18:
			raise MyException(age)
except MyException as e:
	print(e)


finally:
	pass