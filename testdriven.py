class test:
    def __init__(self,name,age,city) -> None:
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name,self.age,self.city)
        
class test1(test):
    def __init__(self, name, age, city) -> None:
        super().__init__(name, age, city)      # super() is used to call parent class constructor.
        
    
t1=test1("raj",24,"chennai")   #object created by using child class
t1.display()    # method in parent classs 

t2=test1("jhon",24,"chennai")   #object created by using child class
t2.display()    # method in parent classs 
