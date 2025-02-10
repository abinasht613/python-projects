from collections import Counter

mylist	=	[1,2,3,4,5,5,5,6,6]
mycounter	=	Counter(mylist)
print(mycounter)
# print(mycounter.keys())
# print(mycounter.values())
maxkey	=	max(mycounter,key=mycounter.get)			# single duplicate element & no of repeat
print(f"{maxkey}--{mycounter[maxkey]}")


duplicateList	=	[]									# multiple duplicate and no of repeat
for k in mycounter.keys():
	if mycounter[k] > 1:
		duplicateList.append({k:mycounter[k]})

print(duplicateList)



