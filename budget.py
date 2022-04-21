class Category:

  ledger = []
  
  def __init__(self, name):
    self.name = name

  def deposit (self, amount, description = ""):
    Category.ledger.append({"amount": amount, "description": description})

  
  def withdraw(self, amount, description = ""):
    funds = 0
    for i in range(len(Category.ledger)):
      funds += Category.ledger[i]['amount']

    if amount <= funds :
      Category.ledger.append({"amount": - amount, "description": description})
      return True
    else :
      return False

  def get_balance(self):
    balance = 0
    for i in range(len(Category.ledger)):
      balance += Category.ledger[i]['amount'] 
    return balance

  
  def check_funds(self, amount):
    if amount > self.get_balance() :
      return False
    else :
      return True  
      

    
    



def create_spend_chart(categories):
  print("")
