class Dog:
    def speak(self):
        print("Dog says Woof")


class Cat:
    def speak(self):
        print("Cat says Meow")


class Person:
    def speak(self):
        print("Person says Hello")


def make_it_speak(animal):
    animal.speak()


make_it_speak(Dog())
make_it_speak(Cat())
make_it_speak(Person())