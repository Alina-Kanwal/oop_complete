class Car:
    def __init__(self, name , model):
        self.name = name
        self.model = model

    def full_info(self):
        return f"{self.name} {self.model}"

my_car = Car("Toyota" , "safari") 
print(my_car.name)  
print(my_car.model)        
print(my_car.full_info()) # We use paranthesis because model_name is an function

#Inheritence in python

"""inheritence ko hum yhn virasat lyskty hain yani aik function ko dosry function say connect krwa kr phly function ki
properties ko gain krty hain"""

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
       super().__init__(brand, model)  # super ky through hum ny brand or model ko access krlya hy yani uper w
       self.batterysize = batterysize  # aly function ki properties ko

electricCar = ElectricCar("Tesla" , "Model S" , "85KWH") 
print(electricCar.batterysize) 
print(electricCar.model_name)


#///////////////////////////////////////////////////////////////////////////Practise

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def fullinfo(self):
        return f"{self.name} {self.model}"   

my_car = Car("Toyota", "safari")
print(my_car)

class ElectricCar(Car):
    def __init__(self , name, model, batterysize):
        super().__init__(name, model)
        self.batterysize = batterysize


electricCar = ElectricCar("Tesla" , "Model S" , "85KWH")
print(electricCar.batterysize)
print(electricCar.fullinfo())


        


        