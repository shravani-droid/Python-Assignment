# write a program which displays 5 times Marvellous on screen.
# output: Marvellous
#         Marvellous
#         Marvellous
#         Marvellous
#         Marvellous

def Display():
    for ch in range(1,6):
        print("Marvellous")
    return Display

def main():
    Ret = Display()

if __name__ == "__main__":
    main()