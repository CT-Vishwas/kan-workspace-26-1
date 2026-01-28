class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    # def get_balance(self):
    #     return self.__balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance

acc = Account("Alice", 1000)
acc.deposit(500)
# print(acc.get_balance())
print(acc.balance)