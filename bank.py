class Account():

    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Успешно пополнили счет. Сумма на счету - {self.balance}')

    def withdraw(self, money):
        if money > self.balance:
            print(f'Недостаточно средств на счету')
        elif money <= self.balance:
            self.balance -= money
            print(f'Вы успешно сняли {money} рублей. Остаток на счету: {self.balance}')

    def all_balance(self):
        print(f'Текущий баланс - {self.balance}')

man = Account('123456789', 800)

man.all_balance()
man.withdraw(450)
man.withdraw(1000)
man.deposit(23000)




