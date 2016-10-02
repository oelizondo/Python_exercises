class Account:
    def __init__(self, name, balance):
        self.name    = name
        self.balance = balance

    def deposit(self, amount):
      self.balance += amount

    def extract(self, amount):
      if self.balance < amount:
        return False
      else:
        self.balance -= amount

    def transfer(self, target, amount):
      target.deposit(amount)
      self.extract(amount)

    def print_me(self):
        print(self.name)
        print(self.balance)
