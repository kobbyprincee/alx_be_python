class BankAccount:

    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.account_deposit = 0
        self.withdrawn_amount = 0
        
        # deposit(amount) 
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            self.account_deposit += amount

        else:
            raise ValueError("Deposit amount must be a positive amount")
        
        # withdraw(amount)
    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Amount must be a positive figure")
        
        elif self.account_balance >= amount:        
            self.account_balance -= amount 
            self.withdrawn_amount += amount
            return True
        else:
            return False
        
        # display_balance()
    def display_balance(self):  
        # print(f"Funds deposited: ${self.account_deposit}") 
        # print(f"Funds withdrawn: ${self.withdrawn_amount}") 
        print(f"Current Balance: ${self.account_balance:.2f}") 
