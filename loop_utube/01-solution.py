# class userinformation:
#     #self reserved keyword hy joky apny class variable ko refer krta hy __init__ aik constructor hy 
#     #jb class my function bunta hy tw constructor lgta hy
#     #instance is object
#     def __init__(self, username, usernic):
#         self.username = username
#         self.usernic = usernic

# userinfo = userinformation("Alina" , "655365")  
# print(userinfo.username) 
# print(userinfo.usernic)   

# # secuserinfo = userinformation("Aliza", "65656565")
# # print(secuserinfo.username)
# # print(secuserinfo.usernic)

#How to add functionality
class Car:
    def __init__(self, name , model):
        self.name = name
        self.model = model  #An attribute is a value or property that is stored inside an object. jaisy self.model

    def model_name(self):
        return f"{self.name} {self.model}"

my_car = Car("Haya" , "safari") 
print(my_car.name)  
print(my_car.model)        
print(my_car.model_name()) # We use paranthesis because model_name is an function

   















        
    





        
