# write a program which accepts the file name from user and 
# display the content of the file line by line on the screen
# Input: Demo.txt
# Output: Display each line of Demo.txt one by  one

def main():
    try:
        file = input("Enter the file name : ")

        file1 = open(file,"r")

        Data = file1.read()

        print(f"The each line of file {file} are displayed as follow :\n",Data)

    except FileNotFoundError as fobj:
        print("File dose not exist")



    

if __name__ == "__main__":
    main()
