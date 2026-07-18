# Write a python to implement a class named Demo with the following specifications: 
# 1. The class contains two instance variables:no1 and no2. 
# 2. The class should contains one class variable and Value.
# 3. Define a constructor(__init__)that accepts two parameters and 
# initialize the instance variables.
# 4. Implement two instance method: 
#       * Fun()- displays the value of instance variable no1 and no2 
#       * Gun()-displays the value of instance variable no1 and no2
#  obj1=Demo(11,21)
#  obj2=Demo(51,101)

class Demo:
    Value = 19

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Inside Instance Method Named As Fun")
        print(self.no1)
        print(self.no2)

        print(self.Value)

    def Gun(self):
        print("Inside Instance Method Named As Gun")
        print(self.no1)
        print(self.no2)
        
        print(self.Value)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
