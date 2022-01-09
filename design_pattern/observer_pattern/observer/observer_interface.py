from abc import ABC, abstractmethod

class IObserver(ABC):

    @abstractmethod
    def update(self, absence:str, designee:str):
        pass
