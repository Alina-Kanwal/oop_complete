#property decorators
#for making it read only yani read krlo but change na krsako
class Car:
    def __init__(self , name, model):
        self.name = name
        self.__model = model

    #class ky under function banaya jayee us class variable name say Property decorator say 
    @property 
    def model(self):
        return self.__model

       
#Change hogya mode AB kis trhn isko change hony say roka jayy        
my_car = Car("Toyota", "safari")
my_car.model = "city"
print(my_car.model)   #get we error as we can't change it

# print(my_car.model()) #isko hum as a function call ni krskty


class book:
    def __init__(self, bookname, totalbooks):
        self.__bookname = bookname
        self.totalbooks = totalbooks

    @property
    def bookname(self):
        return self.__bookname


class book2(book):
    def __init__(self , bookname, totalbooks):
        super.__init__(bookname,totalbooks) 

Book = book("my history" , "4")  
Book.__bookname = "hello"                #Now we can't change
print(Book.__bookname) 


class Battery:
    pass #The pass statement tells Python: “Do nothing here for now.”
         #This is often used when you're planning to implement something later.



        










