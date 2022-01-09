from abc import ABC, abstractmethod
class ShoutInterface(ABC):
    @abstractmethod
    def shout(self):
        pass
    
class DogShout(ShoutInterface):
    def shout(self):
        print('wowowo')
        
class CatShout(ShoutInterface):
    def shout(self):
        print('meow')
        
class BirdShout(ShoutInterface):
    def shout(self):
        print('juju')
        
shout_list = []
shout_list.append(DogShout())
shout_list.append(CatShout())
shout_list.append(BirdShout())
for animal in shout_list:
    animal.shout()