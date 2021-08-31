class Vehicle:
    #properties
    make = None
    model = None
    count = 0

    #Private variable
    __wheels = None

    #Protected Variable
    _seats = None

    #constructor
    def __init__(self,make=None,model=None,wheels=None):
        self.make = make
        self.model = model
        self.__wheels = wheels
        self.count += 1

    # def __init__(self):
    #     print("Inside default constructor")

    #behaviours
    def start(self):
        print(f"Vehicle {self.make} {self.model} is starting.")

    def get_info(self):
        print("Make: "+self.make + " Model: "+self.model + " Wheels:", self.__wheels)

    def get_seats(self):
        print("Seats: "+str(self._seats))

    #Static Method
    # @staticmethod
    # def get_count(self):
    #     return self.count;

    @staticmethod
    def printInfo1():
        print("something")

class Car(Vehicle):
    #attributes
    wheels = 4
    doors = None

    def __init__(self,make,model,doors):
        super().__init__(make,model,self.wheels)
        self.doors = doors

    def open_door(self,door_number):
        print("Opening door", door_number)

    #Overriding from parent class
    def get_info(self):
        print("Make: "+self.make + " Model: "+self.model + " Wheels:", self.wheels, "Doors:", self.doors)


v1 = Vehicle(wheels=4)
v1.make = "Honda"
v1.model = "City"
#v1.__wheels = 4;
v1.get_info()
v1.start()
v1._seats = 2;
v1.get_seats()

v2 = Vehicle("Toyota","Camry",4)
v2.get_info()
v2.get_info()

v1.printInfo1()
print(Vehicle.count)

#get_info(v1)
c1 = Car("Tata","Safari","4")
c1.get_info()