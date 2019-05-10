class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount()
b = BankAccount()
print('Current balance for a:',a.deposit(100))
print('Current balance for b:',b.deposit(50))
print('Current balance for b:',b.withdraw(10))
print('Current balance for a:',a.withdraw(10))
