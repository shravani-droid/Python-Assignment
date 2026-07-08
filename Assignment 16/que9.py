# write a program which displays the first 10 even numbers on screen.

def DispEven():
    for i in range(1,21):
        if(i % 2 == 0):
            print(i,end = " ")
    return DispEven

def main():
    DispEven()

if __name__ == "__main__":
    main()