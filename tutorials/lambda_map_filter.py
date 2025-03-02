mylabbda = lambda a,b: a+b

print(mylabbda(2,3))

mylist = [1,2,3,4,5,6]

odd_even = list(filter(lambda x:x%2==0,mylist))
print(odd_even)

sq_num = list(map(lambda x:x**2,mylist))
print(sq_num)