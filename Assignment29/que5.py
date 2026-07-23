# write a program which accepts a file name and one string 
# from the user and returns the frequency(count of occurrence) of that string in the file.
# Input: Demo.txt Marvellous
# Output: count how many times "Marvellous" appears in Demo.txt

import sys

def ChkWord(FileName,word):
    try:
        file = open(FileName,"r")

        Data = file.read()

        count = Data.count(word)

        print("Frequency of",word, "is" , count) #inbuilt function
                
    except FileNotFoundError as e:
        print("File is not present in current directory")    

def main():
    f1 = (sys.argv[1])
    f2 = (sys.argv[2])
     

    ChkWord(f1,f2)

if __name__ == "__main__":
    main()
