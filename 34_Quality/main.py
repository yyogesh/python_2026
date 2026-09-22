def calculate_total(items, discount=None, tax=None, customer=None):
    total = 0

    if items:
        for item in items:
            if item["price"] > 0:
                if item["quantity"] > 0:
                    total += item["price"] * item["quantity"]

    if discount:
        if customer:
            if customer["type"] == "premium":
                total = total - total * discount * 0.20
            else:
                total = total - total * discount

    if tax:
        total += total * tax

    return total


# linting and formatting

# ruff


# Developer
#    │
#    ▼
# Write Code
#    │
#    ▼
# Ruff
#  ┌─┴───────────────┐
#  │                 │
# Linting        Formatting
#  │                 │
#  └───────┬─────────┘
#          ▼
#      Pytest
#          │
#          ▼
#  Complexity Check
#          │
#          ▼
#  Documentation
#          │
#          ▼
#  Git Commit
#          │
#          ▼
#  Pre-commit Hooks
#          │
#          ▼
#  GitHub Actions
#          │
#          ▼
#        PR


# flake8
# isort
# Black
# pycodestyle
# pyflakes

# Ruff
#  ├── linting
#  ├── formatting
#  └── import sorting

# uv add --dev ruff
# pip install ruff


# src/
#     calculator.py

# ruff check .

# F401 imported but unused
# E501 line too long
# F841 local variable assigned but never used

# ruff format .

# def calculate_total(a,b,c):
# def calculate_total(a, b, c):

#pyproject.toml

# [tool.ruff]
# line-length = 88

# [tool.ruff.lint]
# select = [
#     "E", # pycodestyle errors
#     "F", #Pyflakes
#     "I", # import sorting
# ]

# [tool.ruff.format]
# quote-style = "double"



def process(value):
    if value > 10:
        print("large")

    return value


# if
# if
# for
# while

def process_order(order):
    if order:
        if order["customer"]:
            if order["customer"]["active"]:
                if order["items"]:
                    for item in order["items"]:
                        if item["price"] > 0:
                            if item["quantity"] > 0:
                                if item["in_stock"]:
                                    process(item)



# Complexity	Interpretation
# 1–5	Usually simple
# 6–10	Moderate
# 11–15	High
# 16+	Very high


# pip install radon
# radon cc src/ -s

# src/calculator.py
#     calculate_total - B (8)


# if customer:
#     if customer.active:
#         if customer.country == "IN":
#             process(customer)


# if not customer:
#     return

# if not customer.active:
#     return

# if customer.country != "IN":
#     return

# process(customer)


# The 20-Line Heuristic


# def create_customer():
#     # validate input
#     # calculate discount
#     # save database
#     # send email
#     # write audit log
#     # publish event
#     # generate PDF
#     # ...


# x = p * q

# total_price = unit_price * quantity

# active_customers # ac


# Add price and quantity
# total = price * quantity


def calculate_total(
    unit_price: float,
    quantity: int,
) -> float:
    """Calculate the total price for an item."""
    return unit_price * quantity


def calculate_total(
    unit_price: float,
    quantity: int,
) -> float:
    """Calculate total price.

    Args:
        unit_price: Price of one item.
        quantity: Number of items.

    Returns:
        Total price.
    """
    return unit_price * quantity


calculate_total(
    unit_price=10.0,
    quantity=5,
)



def calculate_total(unit_price, quantity):
    """
    Calculate total price.

    Parameters
    ----------
    unit_price : float
        Price of one item.
    quantity : int
        Number of items.

    Returns
    -------
    float
        Total price.
    """


def calculate_total(unit_price, quantity):
    """
    Calculate total price.

    :param unit_price: Price of one item.
    :param quantity: Number of items.
    :return: Total price.
    """

# mkdocs serve
# docs/
#     index.md
#     architecture.md
#     api.md



def add(a, b):
    """Add two numbers.

    >>> add(2, 3)
    5

    >>> add(10, 20)
    30
    """
    return a + b


# python -m cProfile script.py