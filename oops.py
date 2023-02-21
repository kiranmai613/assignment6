# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.

class Dog:

    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def description(self):
        return f"name is {self.name} and age is {self.age}"
    
    def get_info(self):
        return f" coat color is {self.coat_color} "
    
#c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.

class JackRussellTerrier(Dog):    #inherit parent class Dog
    
    def Jack(self,food):
        self.food=food
        
        print("food it eats is ",self.food)  
    
        

class Bulldog(Dog):          # inherits parent class Dog
        
    def Bull(self,color):
        self.color=color
        
        print("Its color is : ",self.color)


JackRussell=JackRussellTerrier("nicy","7mnths","grey") 

print(JackRussell.description())
print(JackRussell.get_info())
JackRussell.Jack("chkn")



Bull=Bulldog("baby","6mnths","black")
print(Bull.description())
print(Bull.get_info())
JackRussell.Jack("apple")

