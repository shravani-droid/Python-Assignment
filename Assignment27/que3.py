# Write a program to impleanment a class name Numbers

class Numbers:
    def __init__(self,Value):
        self.Value = Value
        self.Value = int(input("Enter the number : "))

    def ChkPrime(self,No):
        if (No <= 1):
            return False
    
        for i in range(2,(No//2) + 1):
            if(No % i == 0):
                return False
            
        return True


    def ChkPerfect(self):

    def Factors(self):

    def SumFactors(self):    