class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []


  def deposit (self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  
  def withdraw(self, amount, description = ""):
    funds = 0
    for i in range(len(self.ledger)):
      funds += self.ledger[i]['amount']

    if amount <= funds :
      self.ledger.append({"amount": - amount, "description": description})
      return True
    else :
      return False

  def get_balance(self):
    balance = 0
    for i in range(len(self.ledger)):
      balance += self.ledger[i]['amount'] 
    return balance

  
  def check_funds(self, amount):
    if amount > self.get_balance() :
      return False
    else :
      return True  

  def transfer(self, amount,  otherBudget):
    if amount > self.get_balance() :
      return False
    else :
      self.withdraw(amount,"Transfer to " + otherBudget.name)
      otherBudget.deposit(amount,"Transfer from " + self.name)
      return True 
      
        
    
    



def create_spend_chart(categories):
  print("")
