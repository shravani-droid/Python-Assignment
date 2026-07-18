# Write a program to impleanment a class name BankAccount

class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount


    def Deposit(self):
        Amount_dep = int(input("Enter the amount for deposit : "))
        self.Amount = self.Amount + Amount_dep
    
    def Withdraw(self):
        Withdraw_amt = int(input("Enter the amount to withdraw from account :"))
        if Withdraw_amt < self.Amount:
            self.Amount = self.Amount - Withdraw_amt
        else:
            print("Insuffcient balance in account")

    def Display(self):
        print("Account Holder name  : ",self.Name)
        print("Current Balance : ",self.Amount)

    def CalculateIntrest(self):
        Intrest = (self.Amount * BankAccount.ROI)/100
        return Intrest
def main():

    boj1 = BankAccount("Ashok",5000)
    #boj2 = BankAccount("Neha")

    boj1.Display()
    boj1.Deposit()
    boj1.Display()
    boj1.Withdraw()
    boj1.Display()
    print("Intrest : ",boj1.CalculateIntrest())

if __name__ == "__main__":
    main()


    
        