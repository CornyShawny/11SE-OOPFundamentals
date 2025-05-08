from bank_account import BankAccount

account1 = BankAccount(1908123, 1902.50, 'Yo Gurt')
account2 = BankAccount(1827384, 1023.90, 'Gurt Yo')

print(account1.get_account_number())
print(account1.get_balance())
print(account1.get_owner_name())

print(account2.get_account_number())
print(account2.get_balance())
print(account2.get_owner_name())

account1.set_account_number(3128972)
account1.set_balance(98292313.50)
account1.set_owner_name('Shawn Fan')

account2.set_account_number(1892039)
account2.set_balance(2311232312324.50)
account2.set_owner_name('Bill Gates')

print(account1.get_account_number())
print(account1.get_balance())
print(account1.get_owner_name())

print(account2.get_account_number())
print(account2.get_balance())
print(account2.get_owner_name())
