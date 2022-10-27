#Tested using base class, all passed.

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
