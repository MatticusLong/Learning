#Bank_accounts.py
#define BankAccount class
#Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:first_name (string)
#last_name (string)
#account_id (integer)
#account_type (string)
#pin (integer)
#balance (float)

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
        self.balance += amount

  def withdraw(self, amount):
        self.balance -= amount 

  def display_balance(self):
        print(self.balance)

John = BankAccount('John', 'Doe', 9876, 'Savings', 1234, 1000.0)

# Now we can use the methods defined in the BankAccount class

John.deposit(96)

John.withdraw(25)

John.display_balance()  # This should print the updated balance after deposit and withdrawal
# Expected output: 1071.0
