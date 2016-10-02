from account import Account

class Bank:
  def __init__(self, name):
    self.name = name
    self.accounts_number = 0
    self.accounts = []

  def new_account(self):
    print("Please insert account details: ")
    name = input("Name: ")
    balance = int(input("Starting balance: "))
    self.add_account(Account(name, balance))

  def make_deposit(self):
    account = self.search_for_account()
    amount = int(input("How much would you deposit: "))
    account.deposit(amount)

  def make_withdrawal(self):
    account = self.search_for_account()
    amount = int(input("How much would you withdraw: "))
    account.extract(amount)

  def make_transfer(self):
    account = self.search_for_account()
    account2 = self.search_for_account()
    amount = int(input("How much would you transfer: "))
    account.transfer(account2, amount)

  def check_status(self):
    account = self.search_for_account()
    account.print_me()

  def add_account(self, account):
    self.accounts_number += 1
    self.accounts.append(account)

  def search_for_account(self):
    name = input("What is your account name: ")
    for account in self.accounts:
      if name == account.name:
        return account
    return False