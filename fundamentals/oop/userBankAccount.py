class BankAccount:
    def __init__(self): 
        self.int_rate = 2/100
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance -= (amount + 5)
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        return self
    
class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.bankAccount = BankAccount()
        
    def make_deposit(self, amount):
        self.bankAccount.deposit(amount)
        return self
        
    def make_withdraw(self, amount):
        self.bankAccount.withdraw(amount)
        return self
        
    def get_yield_interest(self):
        self.bankAccount.yield_interest()
        return self
        
    def print_balance(self):
        self.bankAccount.display_account_info()
        return self


kate = User("Kate", "shydlovska@gmail.com")
kate.make_deposit(100)
kate.make_withdraw(15).print_balance()