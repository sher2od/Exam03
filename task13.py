from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")



p1 = PayPalPayment()
p2 = CardPayment()
p1.pay(200)
p2.pay(75)
