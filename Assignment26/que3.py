# write a Program to implement a class named Arithmetic.

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the Value1 : "))
        self.Value2 = int(input("Enter the Value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError:
            print("Exception Occured : Division by Zero not allowed ")
            return None

aobj = Arithmetic()

aobj.Accept()

print("Addition is : ",aobj.Addition())
print("Substraction is :",aobj.Substraction())
print("Multiplication is : ",aobj.Multiplication())
ans = aobj.Division()
if ans is not None:
    print("Division is : ",ans)





    