"""Command line bank account"""

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "%s's balance is $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "Balance is $%.2f" % self.balance
  
  def deposit(self, amount):
    if amount <= 0:
      print "Deposit must be greater than 0 dollars"
    else:
      print "Depositting $%.2f" % amount
      self.balance += amount
      #show_balance(self.name)
      self.show_balance()
  
  def withdraw(self, amount):
    if amount > self.balance:
      print "You don't have that much."
      return
    else:
      print "Withdrawl amount is $%.2f" % self.balance
      self.balance -= amount
      print "Updated balance is $%.2f" % self.balance
    self.show_balance()

my_account = BankAccount("Blaine")
print my_account
print my_account.show_balance()
print my_account
print my_account.deposit(2000)
print my_account.withdraw(1000)
print my_account
