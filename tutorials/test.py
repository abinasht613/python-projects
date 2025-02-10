

def add(a,b):
    sum=a+b
    return sum

mysum   =add(3,5)
# print(f"Sum of two no is {mysum}")

list  =  [
           {
            'name'  :   "pen",
            'des'   :   "write good"
            },
            {
            'name'  :   "cloth",
            "des"   :   "soft"
            }
        ]

mylist =   []
for item in list:
    # print(item)
    mylist.append(item['name'])
    

# print(mylist)


dictName    =   {
    "a":"11","b":"22","c":"33"
}

disList =   []
for key,value in dictName.items():
    if key=="c":
        disList.append(value)

# print(disList)

tup2    =   (
        {
            "b":"1"
        },
        {
            "a":"2"
        }
    )
# print(tup2)

i=1
while i<10:
    # print(i)
    i +=    1



x   = lambda a,b:   a*b
    
# print(x(2,3))


class Person:
    count=0

    def __new__(cls,*args,**kargs):         #new object
        print("new")
        return super().__new__(cls)
    
    def __init__(self,name,age):            #initializa attribute
        print('init')
        self.name = name
        self.age=age
        Person.count+=1

    def __str__(self):
        return f"{self.name}--{self.age}"    

    def myfun(self):
        return f"Myfun- {self.name}"
        
# a = Person("abi",31)        
# b=Person('tal',30)
# c=Person('aa',30)

# print(a.name)
# print(b)
# print(c.myfun())
# print(f"Count= {Person.count}")

class Student(Person):
    def __init__(self,name,age,year):
        super() .__init__(name,age)
        self.gradYear   =year

    def myGrad(self):
        return f"Name= {self.name}, age= {self.age}, grad year= {self.gradYear}"


c=Student('dd',33,"2000")        
# print(c.myGrad())


def add(*args):
    sum=0
    if len(args)==2:
        sum=args[0]+args[1]

    elif len(args)==3:
        sum=args[0]+args[1]+args[2] 

    else:
        pass
    return sum

# print(add(1,2))
# print(add(1,2,3))


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

  def __del__(self):
    print("Car object deleted")

class Boat(Vehicle):
  def move(self):
    print("Sail!")

  def __del__(self):
    print("Boat object deleted")

class Plane(Vehicle):

    def __new__(cls,*args,**kargs):
        print("Plane __new__")
        return super().__new__(cls)

    def __init__(self, manufacturer, model):
        print("Plane __init__")
        
    def __str__(self):
        return "Plane __str__"

    def move(self):
        print("Fly!")

    def __del__(self):
        print("Plane object deleted")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   print(x.move())

print(plane1)
# print(f"---{plane1.move()}")
plane1.move()

# del plane1  #destruction 
