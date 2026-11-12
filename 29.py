class BankAccount:
    def __init__(self):
        self.name = "Kiran"
        self.account_number = 21112122
        self.balance = 20000

    def deposit(self):
        amount = 200
        self.balance += amount
        print("Deposited Amount:", amount)
        print("Total Balance:", self.balance)

    def withdraw(self):
        amount = 300
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn Amount:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


class SBI(BankAccount):
    pass


sbi = SBI()
sbi.deposit()
sbi.withdraw()
sbi.display_balance()
