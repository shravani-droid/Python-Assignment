# write a program which accepts N numbers from user and store it into list.Returns addition of a prime numbers from that list.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is a part of our user defined 
# module named as MarvellousNum. Name of the function from main python files should be ListPrime().



def ChkPrime(No):
    if (No <= 1):
        return False
    
    for i in range(2,(No//2) + 1):
        if(No % i == 0):
            return False
        
    return True
