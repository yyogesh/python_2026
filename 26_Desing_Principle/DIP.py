# Dependency Inversion Principle


class EmailService:

    def send(self, message):
        print("Email:", message)


class OrderService:

    def place_order(self):
        print("Order placed")

        email = EmailService()
        email.send("Order confirmed")


from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailService(NotificationService):

    def send(self, message):
        print("Email:", message)


class SMSService(NotificationService):

    def send(self, message):
        print("SMS:", message)



class OrderService:

    def __init__(self, notification_service):
        self.notification_service = notification_service

    def place_order(self):
        print("Order placed")

        self.notification_service.send(
            "Order confirmed"
        )



order_service = OrderService(EmailService())
order_service.place_order()


order_service = OrderService(SMSService())
order_service.place_order()