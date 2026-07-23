# write a program which accepts a file name from user and 
# counts total numbers of words in that file
# Input: Demo.txt 
# Output: Total numbers of words in demo.txt

def CountFileWords(FileName):
    try:
        file = open(FileName,"r")
        print("File gets open")
        
        count = 0

        for line in file:
            for words in line:
                count = count + 1


        return count
    
    except FileNotFoundError as fobj:
        print("File dose not exist")


def main():
    
    file1 = input("Enter the File name : ")
    Ret = CountFileWords(file1)

    print(f"The total numbers of word in {file1} are : ",Ret)

if __name__ == "__main__":
    main()

