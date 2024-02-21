class ATM:
    def __init__ (self,x,h,hh,f):
        self.account_balance = x
        self.h = h
        self.hh = hh
        self.f = f
        self.listt = []

    def withdraw(self,amount):
        if amount%100 != 0:
            print("Enter Multiples of 100: ")
            return
        if amount <= self.account_balance:
            if amount > 10000:
                otp = int(input("Enter your OTP: "))
                if otp >= 4:
                    self.account_balance -= amount
                    print("Widthdraw Successfull")
            self.account_balance -= amount
            print("Widthraw Successful")
            a = str(amount) + " - Withdrawn."
        else:
            print("Insufficient Funds")

    def deposit(self,amount,h,hh,f):
        if amount%100 != 0:
            print("Enter Multiples of 100: ")
            return
        self.account_balance += self.account_balance
        self.h += h
        self.hh += hh
        self.f += f
        print("Deposited Successfully")
        a = str(amount) + " - Deposited."
        self.listt.append(a)
    
    def miniStatement(self):
        
        for i in (self.listt[-5]):
            print(i)
        




print("WELCOME TO A+ ATM")
atm = ATM(50000,100,100,40)
while(True):
    print("---------------")
    print("1. Widthdraw")
    print("2. Deposit")
    print("3. Mini Statement")
    print("4. Exit")
    print("---------------")

    choice = int(input("Enter your choice : "))
    match choice:
        case 1:
            amount = int(input("Enter Widthdraw Amount"))
            atm.withdraw(amount)
        case 2:
            amount = int(input("Enter Deposit amount: "))
            h = int(input("Enter 100's: "))
            hh = int(input("Enter 200's: "))
            f = int(input("Enter 500's: "))
            atm.deposit(amount,h,hh,f)
        case 3:
            atm.miniStatement()
        case 4:
            exit(0)
    print("--------- Transaction End -----------")
        
        
