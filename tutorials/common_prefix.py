mystring1	=	["abinash","abital","abtalukdar"]		#ab

firstword	=	mystring1[0]
# print(firstword)

myprefix	=	""
for x in range(0,len(firstword)):
	# print(firstword[x])
	check =	False
	for y in mystring1:
		if y[x]!=firstword[x]:
			check=False
			break
		else:
			# print(firstword[x])
			check=True
			
	if not check:
		break
	if check:
		myprefix+=firstword[x]
		# print(myprefix)

print(myprefix)


			




