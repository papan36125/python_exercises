from oop import BankAccount

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print ('Sorry, minimum balance must be maintained.')
        else:
            # print("balance:", self.balance)
            return super().withdraw(amount)

c= MinimumBalanceAccount(20)
print('Current balance for c:',c.deposit(50))
print('Current balance for c:',c.withdraw(40))
print('Current balance for c:',c.deposit(50))
print('Current balance for c:',c.withdraw(20))
