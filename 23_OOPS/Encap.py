class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):

        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value

account = BankAccount(1000)

print(account.balance)
account.balance = -5000

print(account.balance)



def deposit(self, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    self._balance += amount


def withdraw(self, amount):

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > self._balance:
        raise ValueError("Insufficient balance")

    self._balance -= amount


def transfer(self, other, amount):

    self.withdraw(amount)
    other.deposit(amount)




class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, owner, initial_balance=0):
        if not owner:
            raise ValueError("Owner is required")

        if initial_balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)


rahul = BankAccount("Rahul", 1000)
amit = BankAccount("Amit", 500)


#                 BankAccount
#                      │
#              bank_name = ABC Bank
#                      │
#           ┌──────────┴──────────┐
#           ↓                     ↓
#        rahul                   amit
#    ┌─────────────┐        ┌─────────────┐
#    │ owner Rahul │        │ owner Amit  │
#    │ balance 1000│        │ balance 500 │
#    └─────────────┘        └─────────────┘
#           │                     │
#        methods               methods
#           │                     │
#       deposit()             deposit()
#       withdraw()            withdraw()
#       transfer()            transfer()

# __new__  → creates
# __init__ → initializes