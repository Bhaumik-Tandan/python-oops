"""
Question 1: Encapsulation and Abstraction
Create a class BankAccount with private attributes balance and account_number. 
Implement methods to deposit, withdraw, and check balance. 
Ensure that the account number is not directly accessible from outside the class.
"""


class BankAccount:
    def __init__(self,account_number):
        self._balance=0
        self._account_number=account_number

    def deposit(self,deposit_amount):
        self._balance+=deposit_amount

    def withdraw(self,withdraw_amount):
        if self._balance<withdraw_amount:
            return "Insufficient Balance"
        self._balance-=withdraw_amount
        return self._balance
    
    def check_balance(self):
        return self._balance


account=BankAccount(12345)
account.deposit(100)
print(account.withdraw(200))
account.check_balance()
print(account.withdraw(20))

