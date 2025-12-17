# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
            self.balance -= amount
            print(f"Rs. {amount}/- debited")
            print(f"Total Balance = {self.get_balance()}")

    # credit method
    def credit(self, amount):
            self.balance += amount
            print(f"Rs. {amount}/- credited")
            print(f"Total Balance = {self.get_balance()}")

    # printing the balance
    def get_balance(self):
            return self.balance

acc1 = Account(25000, 32953409)
#print(acc1.account_no)
#print(acc1.balance)

acc1.debit(1000)
acc1.credit(25000)

# Also create multiple accounts (objects)