class Bank:
    def __init__(self,accNo,name,accType,balance=0):
        self.acc=accNo
        self.na=name
        self.accType=acccType
        self.bal=balance
    def deposite(self,amount):
        if amount>0:
            self.bal+=amount
            print(f"Deposite successful! New balance:{self.bal}")
        else:
            print("invalid deposite amount.Please enter a positive value.")
    def withdraw(self,amount):
         if amount>0:
            self.bal-=amount
            print(f"withdrawl successful! New balance:{self.bal}")
        else:
            print("invalid balance.")
        else:
            print(f"withdrawl successful! Please enter a positive value.")
    def display(self)
        print(f"Account Number:{self.acc}\n Accoumt Holder Nmae:{self.na}")
        print(f"Account Type:{self.accType}\n Balance:{self.bal}")
        printf("\n***Menu**")
        print("1.Deposit\n2.Withdraw\n3.Display\n4.Exit")
b1 = Bank(1002,"Nidhi","Savings",0)
b1.display()
while true:
    choice = int(input("\nEnter your choice(1-4):"))
    if choice==1:
        d= int(input("\nEnter the amount to be deposited:"))
        b1.deposit(d)
    elif choice==2:
        w=int(input("\nEnter amount to withdraw:"))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice==4:
        print("Exixting.... THank youuuu!")
        breaj
    else:
        print(""Enter a valid choice:)
            
