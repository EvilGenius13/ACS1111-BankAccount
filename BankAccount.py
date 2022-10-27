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
        
def banking_loop():
    bank_loop = True
    while bank_loop:
        user_account_response = input('What would you like to do?: D for Deposit, W for Withdrawal, I for Interest, S for Statement, Q to Quit. ')
        if user_account_response.upper() == 'D':
            deposit_amount = input('How much would you like to deposit?: ')
            deposit_amount = int(deposit_amount)
            new_account.deposit(deposit_amount)
            continue
        elif user_account_response.upper() == 'W':
            withdraw_amount = input('How much would you like to withdraw?: ')
            withdraw_amount = int(withdraw_amount)
            new_account.withdraw(withdraw_amount)
            continue
        elif user_account_response.upper() == 'S':
            new_account.print_statement()
            continue
        elif user_account_response.upper() == 'I':
            new_account.add_interest()
            continue
        elif user_account_response.upper == 'Q':
            bank_loop = False
            
        print(f"Thanks for banking with us. Have a great day!")
        break
             

app_loop = True
while app_loop:
    user_account_response = input('Welcome to EvilGenius Financial ATM. Would you like to create an account? Y/N: ')
    if user_account_response.upper() == 'Y':
        print("Fantastic. Let's get some information from you.")
        user_name = input("Please enter your full name: ")
        new_account = BankAccount(user_name)
        print("\nHere are your account details.\nPlease memorize your account number as it will be hidden on future receipts")
        print(f"Name: {new_account.name}\nAccount Number: {new_account.account}\nBalance: {new_account.balance}")
        banking_loop()
        app_loop = False
    elif user_account_response.upper() == 'N': 
        print("Please visit us again if you would like to bank with us!")
        app_loop = False
    else:
        print("Please enter a valid response (Y/N)")


