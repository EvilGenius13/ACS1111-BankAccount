class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account = account_number
        self.balance = balance
    # TODO: round out balances to not cause crazy decimals
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount withdrawn: ${amount} new balance: {self.balance}")
    def get_balance(self):
        print(f"{self.name}, your balance is: ${self.balance}")
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance = self.balance + interest
        self.balance = round(self.balance, 2)
    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account}\nBalance: ${self.balance}")
        
        

test_account = BankAccount('Joshua Faigan', 1234567, 1000.36)
test_account.deposit(50)
test_account.withdraw(100)
test_account.get_balance()
test_account.add_interest()
test_account.get_balance()
test_account.print_statement()