# write a program which accepts a file name from the user and 
# opens that file and display the entire content on the console
# Input: Demo.txt
# output: Display content of Demo.txt

def DataDisplay(FileName):
    try:
        file = open(FileName,"r")

        Data = file.read()
        
        print(Data)

    except FileNotFoundError as e:
        print("File is not present in the current directory")

def main():
    f1 = input("Enter the file name : ")
    
    DataDisplay(f1)

if __name__ == "__main__":
    main()
