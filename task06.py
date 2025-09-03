class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Summani notogri kiritdingiz")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Yetarli mablag yoq")

    def get_balance(self):
        return self.__balance

ass = BankAccount(250)
ass.deposit(60)
ass.withdraw(45)
print(ass.get_balance())
