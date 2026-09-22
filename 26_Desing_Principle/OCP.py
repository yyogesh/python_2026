# Open/Closed Principle
# Open for extension, closed for modification.

class PaymentService:

    def pay(self, payment_type, amount):

        if payment_type == "upi":
            print(f"Paid ₹{amount} using UPI")

        elif payment_type == "card":
            print(f"Paid ₹{amount} using Card")

        elif payment_type == "cash":
            print(f"Paid ₹{amount} using Cash")

# PayPal
# Bitcoin
# Apple Pay


from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Cash(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


class PaymentService:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def pay(self, amount):
        self.payment_method.pay(amount)


payment_service = PaymentService(UPI())
payment_service.pay(1000)

payment_service = PaymentService(Card())
payment_service.pay(1000)

payment_service = PaymentService(Cash())
payment_service.pay(1000)