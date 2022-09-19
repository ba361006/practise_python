from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name="john", shout_num=1):
        self.name = name
        self.shout_num = shout_num
    def run(self):
        """ implement run behavior"""
        print('run')
    # @abstractmethod
    # def shout(self):
    #     pass
    
class Dog(Animal):
    def __init__(self, name, shout_num):
        super().__init__(name, shout_num)
    def shout(self):
        print('wo' * self.shout_num)

class Cat(Animal):
    def __init__(self, name, shout_num):
        super().__init__(name, shout_num)

dog = Dog('daniel', 3)
dog.run()
dog.shout()