class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Недостаточно Средств")
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
# создаем класс с начальным балансом
# так же создаем депозит который прибавляет деньги к балансу
# делае приватный код на время общедоступным и получаем ответ