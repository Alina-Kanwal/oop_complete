#Multiple inheritance
class Car:
    def __init__(self , name, model):
        self.name = name
        self.model = model

class Engine:
    def engine_info(self):
        return "This is engine"
    
class Battery:
    def battery_info(self):
        return "This is battery"
    
class Electriccar(Car, Engine, Battery):
    pass

electriccar = Electriccar("Toyo" , "safari")
print(electriccar.engine_info())
print(electriccar.name)





    




       