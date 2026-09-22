# Interface Segregation Principle

class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class Robot(Worker):

    def work(self):
        print("Robot working")

    def eat(self):
        raise Exception("Robot doesn't eat")


from abc import ABC, abstractmethod

class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class Human(Workable, Eatable):

    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


class Robot(Workable):

    def work(self):
        print("Robot working")




class Machine(ABC):
    @abstractmethod
    def print_doc(self): pass
    @abstractmethod
    def scan(self): pass
    @abstractmethod
    def fax(self): pass


class Printer(ABC):
    @abstractmethod
    def print_doc(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan(self): pass

class SimplePrinter(Printer):
    def print_doc(self):
        return "Printing..."


class MultiFunctionPrinter(Printer, Scanner):
    def print_doc(self):
        return "Printing..."
    def scan(self):
        return "Scanning..."