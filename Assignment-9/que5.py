# check weather the number is divisible by 3 and 5

def IfDivisible(No1): 
    if(No1 % 3 == 0 and No1 % 5 == 0 ):
        return True
    else:
        return False
        
def main():
    No1 = int(input("Enter the number : "))
    Ret = IfDivisible(No1)
    
    if(Ret == True):
        print("Number is divisible by the 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
    

if __name__ == "__main__":
    main()