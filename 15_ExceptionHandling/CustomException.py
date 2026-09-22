class InsufficientBalanceError(Exception):

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(
            f"Balance={balance}, Requested={amount}"
        )


def withdraw(balance, amount):
    breakpoint()  # Debugging breakpoint
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)

    return balance - amount


try:
    withdraw(1000, 1500)

except InsufficientBalanceError as ex:
    print(ex.balance)
    print(ex.amount)


DEBUG = True
def dprint(*args, **kwargs):
    if DEBUG:
        print('[DEBUG]', *args, **kwargs)
dprint('Starting calculation...')
# When DEBUG=False, all dprint calls