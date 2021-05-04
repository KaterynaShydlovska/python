class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount	

    def make_withdrawal(self, amount):	
        self.account_balance -= amount	

    def display_user_balance(self):
        print(self.name, self.account_balance)
        
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        
        


kate = User("Kate", "email")
mrHulk = User("mrHulk", "email")
andrii = User("Andrii", "email")

kate.make_deposit(100)
kate.make_deposit(100)
kate.make_deposit(100)
kate.make_withdrawal(50)
kate.display_user_balance()

mrHulk.make_deposit(10)
mrHulk.make_deposit(35)
mrHulk.make_withdrawal(5)
mrHulk.make_withdrawal(7)
mrHulk.display_user_balance()


andrii.make_deposit(350)
andrii.make_withdrawal(50)
andrii.make_withdrawal(10)
andrii.make_withdrawal(100)
andrii.display_user_balance()


kate.transfer_money(andrii,50)
kate.display_user_balance()
andrii.display_user_balance()
    