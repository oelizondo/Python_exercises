from bank import Bank

bank = Bank('Bank of America')
done = False

def print_menu():
  print("What woul you like to do?")
  print("1) Open a new account")
  print("2) Make a deposit")
  print("3) Make a withdrawal")
  print("4) Transfer to another account")
  print("5) Check my status")
  print("6) Exit")

def make_decision(answer):
  if answer == 1:
    bank.new_account()
  elif answer == 2:
    bank.make_deposit()
  elif answer == 3:
    bank.make_withdrawal()
  elif answer == 4:
    bank.make_transfer()
  else:
    bank.check_status()

while not done:
  print_menu()
  answer = int(input("Type here: "))
  if answer == 6:
    break
  make_decision(answer)