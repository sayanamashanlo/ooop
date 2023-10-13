class Bank:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def moneyX(self, balance):
        cash = input("Введите сумму:")
        balance += cash
        print("Ваш баланс сотавляет:", cash)

    def _kill(self):
        self.__balance =0

    def __jackpot(self):
        self.__balance *= 10

    def _combimoney(self, other_bank):
        if isinstance(other_bank,Bank):
            self.__balance += other_bank.__balance
            other_bank.__balance = 0
    def __str__(self):
        return self.__balance

Bank.moneyX()
Bank._kill()
Bank.__jackpot = 100
Bank._combimoney()




bank1 = Bank("Мой банк", 100)
bank2 = Bank("Другой банк", 100)




# calic

class Calic:
    def __init__(self, a):
        self.a = a

    def __add__(self, a , other):
        return self.a + other

    def __sub__(self, a,  other):
        other - self.a

    def __mul__(self, a ,  other):
        other * self.a

    def __truediv__(self, a , other):
        other / self.a

c = Calic (12)
c.__add__(12,12)
c.__sub__(12,12)
c.__mul__(12,12)
c.__truediv__(12,12)

