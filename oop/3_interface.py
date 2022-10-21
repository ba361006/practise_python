from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name="john"):
        self.name = name


class ShoutInterface(ABC):
    @abstractmethod
    def shout(self):
        pass


class DogShout(ShoutInterface):
    def shout(self):
        print("wowowo")


class CatShout(ShoutInterface):
    def shout(self):
        print("meow")


class Dog(Animal, DogShout):
    def __init__(self, name):
        super().__init__(name)


dog = Dog("daniel")
print(dog.name)
dog.shout()
