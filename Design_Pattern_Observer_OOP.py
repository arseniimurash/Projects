from os import system
system("cls")

class CentralBankPublisher:

    def __init__(self):
        self.__rates = {"EUR_USD": None, "USD_EUR": None}
        self.__subscribers = []

    def subscribe (self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, name):
        for subscriber in self.__subscribers:
            if subscriber.name == name:
                self.__subscribers.remove(subscriber)
                break

    def notifySubscribers(self):
        for suscriber in self.__subscribers:
            suscriber.update()

    def setRate(self, from_currency, to_currency, rate):
        if from_currency == "EUR" and to_currency == "USD":
            self.__rates["EUR_USD"] = rate
            self.notifySubscribers()
        elif from_currency == "USD" and to_currency == "EUR":
            self.__rates["USD_EUR"] = rate
            self.notifySubscribers()

    def __str__(self):
        return f"BANK RATES:\n {self.__rates}\n {self.__subscribers}"


class Subscriber:

        def __init__(self,name):
            self.name = name

        def __str__(self):
            return f"COMPANY: {self.name}"

        def __repr__(self):
            return self.__str__()

        def update(self):
            print(f"{self.name} GOT THE NOTIFICATION !")

#########################################


cb = CentralBankPublisher()
cb.subscribe(Subscriber("ECB"))
cb.subscribe(Subscriber("EBRD"))
cb.setRate("EUR","USD",1.2)
print(cb)
cb.unsubscribe("EBRD")
print(cb)
cb.subscribe(Subscriber("BNM"))
cb.setRate("USD", "EUR", 0.8)
print(cb)

