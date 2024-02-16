class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient funds"

class SavingsAccount(Account):
    interest_rate = 0.02

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return f"Interest applied. New balance: {self.balance}"

# Example usage
savings_account = SavingsAccount("John", 1000)

print(savings_account.deposit(500))  # Output: Deposited 500. New balance: 1500
print(savings_account.apply_interest())  # Output: Interest applied. New balance: 1530.0
print(savings_account.withdraw(2000))  # Output: Insufficient funds
