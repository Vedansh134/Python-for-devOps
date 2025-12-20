# encapsulation
# Wrapping data and functions into a single unit (object).
# Whenever we create class, inside class have attributes and methods -- encapsulation

class BankAccount:
    def __init__(self, Balance):
        # Public attribute (by default) - generally a bad practice for sensitive data
        self.Account_holder_name = "Vedansh kumar"

        # Private attribute (convention enforced by name mangling)
        self.__balance = Balance

    def deposit(self, amount):
        """Public method to safely modify the balance."""
        if amount > 0:
            self.__balance += amount
            print(f"User deposit amount : {amount}. Now balance : {self.__balance}")
        else:
            print(f"Invalid amount number : {amount}. Enter proper amount")

    def get_balance(self):
        """this functions returns the account balance"""
        return self.__balance

# Usuage
account = BankAccount(1000)
account.deposit(1000) # Accessed via the public method

print(f"Account holder : {account.Account_holder_name}")


# Attempting direct access to the private attribute will raise an AttributeError
try:
    print(f"Account balance : {account.__balance}") # error
except AttributeError as e:
    print(f"Error accessing private attribute directly: {e}")


# Accessing the private attribute through its mangled name (not recommended)
print(f"Access via name mangling: {account._BankAccount__balance}")