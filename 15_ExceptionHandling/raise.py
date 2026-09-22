# Exception chaining: raise a new exception while preserving the original
# Implicit chaining: original exception stored in __context__
try:
    int('abc')         # ValueError
except ValueError:
    raise RuntimeError('Failed to parse config')
    # Traceback shows BOTH: ValueError AND RuntimeError

class ConfigError(Exception): pass

def load_config(path):
    try:
        with open(path) as f:
            return int(f.read())
    except FileNotFoundError as e:
        raise ConfigError(f'Config file missing: {path}') from e
    except ValueError as e:
        raise ConfigError(f'Config value invalid in: {path}') from e




def withdraw(balance, amount):

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


try:
    balance = withdraw(1000, 1500)
    print(balance)

except ValueError as ex:
    print("Error:", ex)





def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


print(withdraw(1000, 1200))