# write a python program to impleanment class named circle with the following requrinments:
# 1. The class should contains three instance variables: Radius,Area and Circumference
# 2. The class should contains one class variable names PI,initialized to 3.14
# 3. Define a constructor (__init__) that initialize all variable to 0.0 
# Implement the following instance method:
#       accept()- accepts the radius of the circle  from the user 
#       calculateArea()- calculates the area of the circle and stores it in the area variable
#       calculatecircumference()-  calculate circumference and stores it in the  circumference variable
#       display()- display the values of radius,area and circumference
# 4. create multiple objects of the circle class and invoke all the instance method for each object

class Circle:
    PI = 3.14
    
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = int(input("Enter the Radius of the Cirlcle: "))

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius
        

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius 
       
    def Display(self):
        print("The Radius of circle is : ",self.radius)
        print("The Area of circle is : ",self.area)
        print("The Circumference of circle is : ",self.circumference)

obj1 = Circle()


obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()
