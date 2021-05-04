class BankAccount:
    def __init__(self): 
        self.int_rate = 1/100
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance -= (amount + 5)
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        return self

accountOne = BankAccount()
accountTwo = BankAccount()

accountOne.deposit(120).deposit(130).deposit(150).withdraw(20).yield_interest().display_account_info()
accountTwo.deposit(300).deposit(30).withdraw(10).withdraw(55).withdraw(11).withdraw(100).yield_interest().display_account_info()
