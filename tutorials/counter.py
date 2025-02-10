from collections import Counter

b = Counter({'geeks' : 4, 'for' : 1, 'gfg' : 2, 'python' : 3})

for x in b.elements():
	print(x,end=" ")

# Counter(f.read().split()).most_common(10)

print (b.values())