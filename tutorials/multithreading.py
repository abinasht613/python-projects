from threading import Thread
import time
import datetime


def myfun1():
	print("f1 start")
	time.sleep(5)
	print("f1 end")

def myfun2():
	print("f2 start")
	time.sleep(2)
	print("f2 end")

def myfun3():
	print("f3 start")
	time.sleep(4)
	print("f3 end")

t1 = Thread(target=myfun1)
t2 = Thread(target=myfun2)
t3 = Thread(target=myfun3)

print(datetime.datetime.now())
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print(datetime.datetime.now())
print("All end")