# write a program which accepts a file name and a word the 
# user and checks wether that word is present in that file or not
# Input: Demo.txt Marvellous
# Output: Display whether the  word Marvellous is found in Demo.txt or not

def ChkWord(FileName,word):
    try:
        file = open(FileName,"r")

        Data = file.read()

        if word in Data:
            return True
        else:
            return False

    except FileNotFoundError as e:
        print("File is not present in current directory")    

def main():
    f1 = input("Enter the name of file : ")
    f2 = input("Enter the word you want to search : ")

    Ret = ChkWord(f1,f2)

    if(Ret == True):
        print(f"The given word '{f2}' is present in file :",Ret)
    else:
        print(f"Given word '{f2}' is not present in file {f1}")


if __name__ == "__main__":
    main()
