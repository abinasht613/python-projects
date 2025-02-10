from collections import Counter

import asyncio

import threading
import time

import os

import random

sentence = "hello hello world"					#1:
word_count	=	Counter(sentence.split())
print(word_count)
for sin in word_count:
	print(f"{sin}--{word_count[sin]}")	



async def fetch_data():						#2: Single thread doesnot block I/O
	print("started")
	await asyncio.sleep(2)
	print("ended")

asyncio.run(fetch_data())




def task(name,delay):						#3: Multi threading
	time.sleep(delay)
	print(f"{name} ended in {delay}")
thread1	=	threading.Thread(target=task,args=["A",2])
thread2 =	threading.Thread(target=task,args=["B",1])
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("All task completed")



numbers	=	[]								#4: Append in List
def add_number(num):
	numbers.append(num)
add_number(5)
add_number(6)
print(numbers)



def is_sorted(lst):							#5: Reverse Sort
	lst.sort(reverse=True)
	return lst
	# return all(lst[i]	<=	lst[i+1] for i in range(len(lst)))

my_seq =	[1,4,2,6,3]
revSorted	=	is_sorted(my_seq)	
print(revSorted)
print(f"Max no is: {revSorted[0]}")


											#6: Sum & Average	
sum=0
for x in revSorted:
	sum +=	x

print(f"avg: {sum/len(revSorted)}")


myfile	=	"./test.py"
print("Current Directory:", os.getcwd())		#7: File
if os.path.exists(myfile):
	with open(myfile, "r") as file:         # Open the file in read mode
		lines = file.readlines()                    # Read all lines
		last_line = lines[-1] if lines else ""
		print(f"Total lines: {len(lines)}")	

		if "del" in last_line:
			print("del found")
		else:
			print("del not")
else:
	print("file not found")




print(random.randrange(1, 10)) 					#8: Random number



def square_decorator(func):						#9: square decorator
	def wrapper(a,b):
		return a**2+b**2
	return wrapper
@square_decorator
def sum(a,b):
	return a+b
print(sum(2,3))



		

def find_missing_element(seq):										#10: find missing no if any
    if len(seq) < 3:
        return None  # Not enough elements to determine a pattern
    
    # Find the actual common difference (smallest difference in the sequence)
    diff = min(seq[i] - seq[i - 1] for i in range(1, len(seq)))
    #4−2=2,	6−4=2,	8−6=2,	10−8=2 			min(2, 2, 2, 2)  # Output: 2
    #5−1=4,	7−5=2,	9−7=2 					min(4, 2, 2)  # Output: 2

    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] != diff:
            return seq[i - 1] + diff  # Return the missing element

    return None  # No missing element

# Test cases
print(find_missing_element([2, 4, 6, 8, 10]))  # Expected: None
print(find_missing_element([3, 6, 9, 15]))  # Expected: 12
print(find_missing_element([1, 3, 7, 9]))  # Expected: 5
print(find_missing_element([1, 5, 7, 9]))  # Expected: 3
print(find_missing_element([2, 4, 6, 10]))	#8