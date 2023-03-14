from os import system
system("cls")

#########################################################
class Bank:
    def __init__(self, balance = 0):
        if type(balance) != int:
            raise TypeError("Only int values")
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        if type(balance) != int:
            raise TypeError("Only int values")
        self.__balance = balance

    def __str__(self):
        return f"BANK: {self.__balance}"
#########################################################
class LocalBank(Bank):
    def __init__(self, location, balance=0):
        super().__init__(balance)
        self.location = location

    def __str__(self):
        return f"LOCAL BANK ({self.location}): {self.getBalance()}"
#########################################################
class CreditBank(Bank):
    def __init__(self, rate, balance=0):
        super().__init__(balance)
        if type(rate) != float:
            raise TypeError("Only float values")
        self.__rate = rate
    
    def getPercent(self):
        return self.__rate

    def setPercent(self, rate):
        if type(rate) != float:
            raise TypeError("Only float values")
        self.__rate = rate

    def maxCreditLimit(self):
        return self.getBalance() - int((self.getBalance() * 0.1))

    def currentDebt(self):
        return self.maxCreditLimit() + int((self.maxCreditLimit() * self.getPercent()))

     
    def __str__(self):
        return f"ECB :\n balance is {self.getBalance()}\n max credit limit is {self.maxCreditLimit()}\n rate (per year) is {self.getPercent()}\n approximate current debt with max credit limit is {self.currentDebt()}\n"
        

#########################################################

world_bank = Bank(100000)
agro = LocalBank("Chisinau", 10000)
ecb = CreditBank(0.05, 1000)

print(world_bank)
print(agro)
print(ecb)

