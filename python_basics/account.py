class Account:
    def __init__(self, name, balance):
        self.name    = name
        self.balance = balance

    def print_me(self):
        print(self.name)
        print(self.balance)
