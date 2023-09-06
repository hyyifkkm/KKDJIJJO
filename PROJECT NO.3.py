class ATM:
    def _init_(self):
        self.Balance = 500

    def choice(self):
        print("1: Balance\n2: Deposit\n3: Withdraw")
        self.l = int(input("Enter your choice: "))
        if self.l == 1:
            print("Balance:", self.Balance)
        elif self.l == 2:
            self.deposit()
        elif self.l == 3:
            self.withdraw()
        else:
            print("Wrong choice!")

    def deposit(self):
        self.n = int(input("Enter the amount of money you want to deposit: "))
        self.Balance += self.n
        print("Balance:", self.Balance)

    def withdraw(self):
        self.m = int(input("Enter the amount of money you want to withdraw: "))
        if self.m > self.Balance:
            print("Insufficient balance")
        elif self.m == self.Balance:
            self.Balance = 0
            print("Balance is now 0")
        else:
            self.Balance -= self.m
            print("Balance:", self.Balance)

o = ATM()
o.choice()
