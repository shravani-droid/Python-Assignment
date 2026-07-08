from que1Module import  *

def main():
    print("Enter first number:")
    Value1=int(input())

    print("Enter second number:")
    Value2=int(input())

    Ret= Add(Value1 , Value2)
    
    print("Addition is : ",Ret)

    Ret= Sub(Value1 , Value2) 

    print("Substraction is :",Ret)

    Ret= Mult(Value1 , Value2) 

    print("Multiplication is :",Ret)

    Ret= Div(Value1 , Value2) 

    print("Division is :",Ret)



if __name__=="__main__":
    main()