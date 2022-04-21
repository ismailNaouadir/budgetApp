# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main


food = budget.Category("Food")
food.deposit(900, "initial deposit")
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")

food.transfer(50, auto)

print(food.get_balance())

'''
food = budget.Category("Food")
food.deposit(900, "deposit")
print(food.ledger)
print(food.get_balance())
print(food.withdraw(45.67))
#food.withdraw(10, "restaurant and more food for dessert")
print(food.ledger)
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)
#print(create_spend_chart([food, clothing, auto]))
'''
# Run unit tests automatically
main(module='test_module', exit=False)
