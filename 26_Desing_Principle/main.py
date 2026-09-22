# Library Management System

# Add books
# Register members
# Search books
# Borrow books
# Return books
# Detect overdue loans
# Save data
# Load data

# Book 
# BookType
# Member
# Loan
# Library
# Searchable 
# Repository

# Entity	Responsibility
# Book	Store book information
# BookType	Define different book categories
# Member	Represent library member
# Loan	Track borrowing
# Library	Coordinate books, members and loans
# Searchable	Define searching contract
# JsonRepository	Save/load data


# class Library:
#     # save JSON
#     # validate members
#     # search
#     # calculate overdue
#     # manage books
#     # manage loans


# Library
#    │
#    ├── Books
#    ├── Members
#    └── Loans

# JsonRepository
#    │
#    └── Persistence

# Searchable
#    │
#    └── Search contract

# Has-A vs Is-A

# Low level design principles

# Is-A → Inheritance
# Has-A → Composition

# EBook IS-A Book
# AudioBook IS-A Book
# PrintedBook IS-A Book

# class EBook(Book):
#     pass


# Has-A → Composition

# Library HAS books
# Library HAS members
# Library HAS loans


# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []
#         self.loans = []


    #                 ┌─────────────────┐
    #                 │   Searchable    │
    #                 │      ABC        │
    #                 └────────┬────────┘
    #                          │
    #                          │ implements
    #                          ▼
    #                 ┌─────────────────┐
    #                 │     Library     │
    #                 ├─────────────────┤
    #                 │ books           │
    #                 │ members         │
    #                 │ loans           │
    #                 ├─────────────────┤
    #                 │ add_book()      │
    #                 │ search()        │
    #                 │ borrow_book()   │
    #                 │ return_book()   │
    #                 └───────┬─────────┘
    #                         │
    #           ┌─────────────┼─────────────┐
    #           │             │             │
    #           ▼             ▼             ▼
    #     ┌──────────┐  ┌──────────┐  ┌──────────┐
    #     │   Book   │  │  Member  │  │   Loan   │
    #     └────┬─────┘  └──────────┘  └──────────┘
    #          │
    #    ┌─────┼─────┐
    #    ▼     ▼     ▼
    #  EBook AudioBook PrintedBook

    #                 Library
    #                    │
    #                    │ uses
    #                    ▼
    #             ┌──────────────┐
    #             │ Repository   │
    #             └──────────────┘
    #                    │
    #                    ▼
    #                 JSON



# library_management/
# │
# ├── pyproject.toml
# ├── README.md
# ├── data/
# │   └── library.json
# │
# ├── src/
# │   └── library_management/
# │       │
# │       ├── __init__.py
# │       ├── __main__.py
# │       │
# │       ├── models/
# │       │   ├── __init__.py
# │       │   ├── book.py
# │       │   ├── member.py
# │       │   └── loan.py
# │       │
# │       ├── types/
# │       │   ├── __init__.py
# │       │   ├── book_type.py
# │       │   ├── ebook.py
# │       │   ├── audiobook.py
# │       │   └── printed_book.py
# │       │
# │       ├── interfaces/
# │       │   ├── __init__.py
# │       │   └── searchable.py
# │       │
# │       ├── repositories/
# │       │   ├── __init__.py
# │       │   └── json_repository.py
# │       │
# │       └── services/
# │           ├── __init__.py
# │           └── library.py
# │
# └── tests/
#     ├── test_book.py
#     ├── test_member.py
#     ├── test_loan.py
#     └── test_library.py

from dataclasses import dataclass


# @dataclass(slots=True)
# class Book:
#     isbn: str
#     title: str
#     author: str
#     available: bool = True


from abc import ABC, abstractmethod


class BookType(ABC):

    @property
    @abstractmethod
    def loan_period(self) -> int:
        pass


class PrintedBook(BookType):

    @property
    def loan_period(self) -> int:
        return 14


class EBook(BookType):

    @property
    def loan_period(self) -> int:
        return 30

class AudioBook(BookType):

    @property
    def loan_period(self) -> int:
        return 21


# BookType
#    │
#    ├── PrintedBook
#    ├── EBook
#    └── AudioBook

# SOLID-style design principles

# Single Responsibility Principle (SRP)
# Open/Closed Principle (OCP)
# Liskov Substitution Principle (LSP) # Subclass must behave like superclass
# Interface Segregation Principle (ISP)
# Dependency Inversion Principle (DIP)




# Single Responsibility Principle (SRP)


class ReportBad:
    def __init__(self, data): self.data = data
    def calculate_total(self): return sum(self.data)
    def save_to_disk(self, path):             
    # a SECOND, unrelated responsibility
        open(path, 'w').write(str(self.calculate_total()))


class Report:
    def __init__(self, data): self.data = data
    def calculate_total(self): return sum(self.data)


class ReportSaver:
    @staticmethod
    def save(report, path):
        open(path, 'w').write(str(report.calculate_total()))

r = Report([1, 2, 3])
r.calculate_total()
ReportSaver.save(r, 'report.txt')


# Open/Closed Principle (OCP) Extend by adding Not modifying 

class Discount(ABC):
    @abstractmethod
    def apple(self, price):
        pass

class NoDiscount(Discount):
    def apply(self, price): return price

class PercentOff(Discount):
    def __init__(self, pct): self.pct = pct
    def apply(self, price): return price * (1 - self.pct / 100)

class XOff(Discount):
    def __init__(self, pct): self.pct = pct
    def apply(self, price): return price * (1 - self.pct / 100)


def checkout(price, discount: Discount):
    return discount.apply(price)

print(checkout(100, NoDiscount()))
print(checkout(100, PercentOff(10)))

# adding a BuyOneGetOne discount later means writing ONE NEW CLASS -
# checkout() above never needs to change, and neither does any EXISTING discount