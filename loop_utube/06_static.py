"""Static method and isinstance
It doesn't receive self (the instance)
It doesn't receive cls (the class)
It is just a plain function that lives inside a class for logical grouping
Same result whether called via class or object

So, it's called static not because of how you access it, but because of how it behaves:
yani y self or cls par depend ni krta ise wja sy iska behaviour static hy yani aik jaisa or unchanging"""

"""Isinstance mtlb ky kea tum, is class ky ho ya ni"""
class Car:
    def __init__(self , name, model):
        self.name = name
        self.model = model

    @staticmethod #is a decorator that inhance the functionality of the method and do many other works
    def general_description():
        return "Cars are multiple types"

class electricCar(Car):
    def __init__(self , name, model, batterysize):
        self.batterysize = batterysize
        super().__init__(name, model)

my_car = Car("Safari" , "toyota")
electriccar = electricCar("toyo" , "safari" , "7865")
print(my_car.general_description())


print(Car.general_description()) #challyga kyu static waly instance ko class say access kea hy

#isinstance
print(isinstance(electriccar, Car))  
print(isinstance(electriccar, electricCar))  

