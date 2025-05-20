"""Question: Add a class variables to car that keeps track of the number of cars created"""
class Car:

    total_car = 0

    def __init__(self, name, model):
        self.name = name
        self.model = model
        Car.total_car += 1

    def fuel(self):
        return "fuel or disel"


class electriccar(Car):
    def __init__(self , name, model, batterysize):
        self.batterysize = batterysize
        super().__init__(name, model)

    def fuel(self):
        return "Electric charges" 


    

mycar1 = Car("Toyota", "safari") 
mycar2 = Car("Toyota", "Nexon") 

print(Car.total_car)


Electriccar = electriccar("Tesla" , "Model S" , "85KWH")  



