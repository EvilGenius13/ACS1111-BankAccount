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
        if self.balance >0:
            interest = self.balance * 0.00083
            self.balance = self.balance + interest
            self.balance = round(self.balance, 2)
    def print_statement(self):
        hide_account = self.balance
        #print(hide_account) - works
        hide_account = str(hide_account)
        #print(hide_account) - works
        hide_account = (hide_account[4:8])
        print(hide_account)
        print(f"{self.name}\nAccount No.: {self.account}\nBalance: ${self.balance}")
        
        
        

mitchell_account = BankAccount('Mitchell Hudson')
mitchell_account.print_statement()
dani_account = BankAccount('Dani Roxberry')
braus_account = BankAccount('Adam Braus')
bank_account = 84582949
bank_account = str(bank_account)
hides_account = (bank_account[4:8])
print(hides_account)