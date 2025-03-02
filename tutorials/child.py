from Parent  import Parent
from collections import Counter
import datetime
import math
import json
import re

class Std(Parent):
	def myfun(self):
		print('Std myfun')

	def myfun1(self):
		super().myfun1()
		# print("Std myfun1")


	def counterA(self,str):

		myCount	=	Counter(str)
		print(myCount)
		max_item	=	{
			'item'	:	"",
			'tot'	:	0
		}
		for sin in myCount.keys():
			print(f"{sin}--{myCount[sin]}")
			if myCount[sin] > max_item['tot']:
				max_item['item']	=	sin
				max_item['tot']		=	 myCount[sin]			
		print(f"Maximum element is: {max_item['item']}---{max_item['tot']}")


	def counterList(self,list):
		myListCounter	=	Counter(list)
		for x in list:
			if myListCounter[x]==1:
				return x
		# print(myListCounter)


a=Std()
# a.myfun()
# a.myfun1()

# a.counterA("abbbccdadddd")

b=a.counterList(["a","a","b","b","b","b","c","c","d"])
# print(f"first: {b}")

unsorted	=	[7,1,5,9,3,6]
sortedd=	sorted(unsorted)

# print(sortedd==unsorted)

# print(datetime.datetime.now().year)
# print(datetime.datetime.now().strftime("%B"))


# print(min(2,1,5))

# print(math.sqrt(4))


myjson	=	'{"namae":"abi","age":"31"}'
# print(json.loads(myjson))

mydict	=	{
	'name':"tal","age":32
}

# print(json.dumps(mydict))


listInsideDistionary	=	{
	'name':"abinash",
	"age":31,
	"education":[
		{
			'title':"MCA",
			'year'	:"2018"
		},
		{
			'title':"BCA",
			"year":"2016"	
		}
	]
}
# print(json.dumps(listInsideDistionary,indent=4))



txt = "My Name is Abinah Talukdar"

print(re.search("^My Name",txt))

try:
	pass
except:
	pass
finally:
	pass

mytype	=	type("5")
print(mytype)




# myInput	=	input("what is your Name?")
# print(f"Your name is {myInput}")

print(f"expression: {2*3+4}")

myname	=	"Abi"
age=31
multiplePlaceHolder = "My Name is {} age is {}"
print(multiplePlaceHolder.format(myname,age))




