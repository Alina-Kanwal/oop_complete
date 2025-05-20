''' Encapsulation ko capsule ki trhn lay skty jo upar say 1 jaisy nazar aty hain mgr hkeekt 
my sub ka kaam different hota hy'''
'''Encapsulation mtlb kesi ki access my rehny na dena aik chez ko aik method ky through access krny dena wrna ni'''
'''Encapsulate means access roknaa,Laken usy hum uski apni class my access krskty hain by 2 methods
1. Getter for // Access k lea
2. Setter for // update k lea'''

class Car:
    def __init__(self, name, model):
        self.__name = name # __ hyphen use kr encapsulate krdea name ko
        self.model = model 

    # Now encapsulate wal class attribute hy usko hum get method ky through get krrhy hain
    def get_name(self):
        return f"{self.__name} " 
    

    # Now encapsulate wal class attribute hy usko hum set method ky through update krrhy hain
    def set_name(self , newname):
        self.__name = newname
      
    
class electricCar(Car):
    def __init__(self, name, model, batterysize):
        super().__init__(name, model)
        self.batterysize = batterysize


'''Yahan par access ni horha class say bahar name ko upar encapsulate krdea hay'''
# print(ElectricCar.__name)


my_car = Car("Toyota", "safari") 
print(my_car.get_name())  # name ko get krlia

my_car.set_name("Toyo")
print(my_car.get_name())  #update name hasil kea

#//////////////////////////////////Practise

class User_info:
    def __init__(self ,user_name, nic_no):
        self.__user_name = user_name
        self.nic_no = nic_no

    def get_username(self):
        return self.__user_name
    
    def set_user_name(self , newname):
        self.__user_name = newname
        
user_info = User_info("Alina" , "5656" )
print(user_info.get_username()) 

user_info.set_user_name("Aleena")
print(user_info.get_username()) 

# class Student_info(User_info):
#     def __init__(self, user_info, nic_no , roll_num):
#         super().__init__(user_info, nic_no)
#         self.roll_num = roll_num


# studentinfo = Student_info("Aliza" , "5656" , "4222")     
# print(studentinfo.user_info)
# print(studentinfo.roll_num)






        
 