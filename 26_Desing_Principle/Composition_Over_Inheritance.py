# Car IS-A Engine
# Car HAS-A Engine


class Engine:
    def start(self):
        print("Engine started")


class Car(Engine):
    def drive(self):
        print("Car is driving")


car = Car()

car.start()
car.drive()



class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")

car = Car()
car.drive()



class ElectricEngine:
    def start(self):
        print("Electric engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is driving")


car = Car(ElectricEngine())

car.drive()