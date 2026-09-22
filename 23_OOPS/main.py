# BankAccount
# │
# ├── DATA → owner, balance
# │
# └── BEHAVIOR → deposit(), withdraw(), transfer()

# Class = blueprint
# Object = actual thing created from blueprint
# Attribute = object's data
# Method = object's behavior

# class BankAccount:
#     pass


# account1 = BankAccount('Aman', 1000)
# account2 = BankAccount('Riya', 2000)

        #            BankAccount
        #                 │
        #     ┌──────────┴──────────┐
        #     ↓                     ↓
        # account1               account2
        # Rahul                  Amit
        # ₹1000                  ₹5000


# BankAccount()
#      │
#      ↓
#   __new__()
#      │
#      ↓
# creates object
#      │
#      ↓
#   __init__()
#      │
#      ↓
# initializes object


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance


# a1 = BankAccount("Rahul", 1000)
# a2 = BankAccount("Amit", 5000)

# print(a1.balance)
# print(a2.balance)


# a1
#  ├── owner → Rahul
#  └── balance → 1000

# a2
#  ├── owner → Amit
#  └── balance → 5000



# Attributes
# │
# ├── Instance attributes
# │
# └── Class attributes


class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

a1 = BankAccount("Rahul", 1000)
a2 = BankAccount("Amit", 5000)



print(a1.bank_name)
print(a2.bank_name)
print(BankAccount.bank_name)

a1.deposit(500)
BankAccount.deposit(a1, 1000)


#            BankAccount
#                  │
#           bank_name = ABC Bank
#                  │
#        ┌─────────┴─────────┐
#        ↓                   ↓
#       a1                   a2
#    Rahul/1000           Amit/5000


# instance => class => Parent class


print(a1.__dict__)
print(a2.__dict__)
print(BankAccount.__dict__)

# Method



class BankAccount:

    bank_name = "ABC Bank"

    @classmethod
    def change_bank(cls, name):
        cls.bank_name = name


BankAccount.change_bank("XYZ Bank")
print(BankAccount.bank_name)




class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_dict(cls, data):
        return cls(data["owner"], data["balance"])


data = {
    "owner": "Rahul",
    "balance": 5000
}

account = BankAccount.from_dict(data)



class BankAccount:

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0



BankAccount.is_valid_amount(1000)
BankAccount.is_valid_amount(-1000)

a1 = BankAccount()

a1.is_valid_amount(1000)
a1.is_valid_amount(-1000)


# Encapsulation

class BankAccount:

    def __init__(self, _balance):
        self._balance = _balance


a1 = BankAccount(1000)
a1._balance

a1._balance = -5000

# __balance




class BankAccount:

    def __init__(self):
        self.__balance = 1000


a1 = BankAccount()
a1.__balance



class BankAccount:

    def __init__(self):
        self.__balance = 1000

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def balance(self, value):

        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value


a1 = BankAccount()
print(a1.__balance)
a1.get_balance()