import random

class BankAccount:
    def __init__(self, full_name,):
        self.name = full_name
        self.account = random.randint(80000000, 89999999)
        self.balance = 0
    # TODO: round out balances to not cause crazy decimals
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <0:
            self.balance -= 10
            print(f"Insufficient funds. You have been charged $10. New balance is: ${self.balance}")
        else:
            print(f"Amount withdrawn: ${amount} new balance: {self.balance}")
    
    def get_balance(self):
        print(f"{self.name}, your balance is: ${self.balance}")
        return self.balance
    
    def add_interest(self):
        if self.balance >=0:
            interest = self.balance * 0.00083
            self.balance = self.balance + interest
            self.balance = round(self.balance, 2)
        else:
            print('You can not earn interest on overdraft balances')
    
    def print_statement(self):
        hide_account = str(self.account)
        hide_account = (hide_account[4:8])
        hide_account = f"****{hide_account}"
        print('--------------------')
        print(f"{self.name}\nAccount No.: {hide_account}\nBalance: ${self.balance}")
        print('--------------------')

mitchell_account = BankAccount('Mitchell Hudson')
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()

dani_account = BankAccount('Dani Roxberry')
dani_account.deposit(5000)
dani_account.withdraw(1500)
dani_account.print_statement()

braus_account = BankAccount('Adam Braus')
braus_account.deposit(50)
braus_account.withdraw(50)
braus_account.withdraw(10)
braus_account.add_interest()
braus_account.print_statement()
