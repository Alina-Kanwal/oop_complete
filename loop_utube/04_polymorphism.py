'''Polymorphism allows us to:
We can put methods with the same name in different classes.
We can use objects in a similar way, even though they are of different types'''

class Car:
    def __init__(self , name, model):
        self.name = name
        self.model = model

    def fueltype(self):
        return "Petrol or disel "                         #Ye aik he name ka obj aik yahan hy   

class electricCar(Car):
    def __init__(self , name, model, batterysize):
        self.batterysize = batterysize
        super().__init__(name, model)

    def fueltype(self):
        return "Electric charges"                            #Or 1 y hy

ElectricCar = electricCar("Tesla" , "Model S" , "85KWH")
print(ElectricCar.fueltype())

my_car = Car("Toyota", "safari") 
print(my_car.fueltype())

