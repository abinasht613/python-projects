import asyncio
import datetime

async def myfun1():
	print("1 started")
	await asyncio.sleep(5)
	print("1 ended")

async def myfun2():
	print("2 started")
	await asyncio.sleep(2)
	print("2 ended")

async def myfun3():
	print("3 started")
	await asyncio.sleep(3)
	print("3 ended")



async def main():
	await asyncio.gather(myfun1(),myfun2(),myfun3())

print(datetime.datetime.now())
asyncio.run(main())
print(datetime.datetime.now())
