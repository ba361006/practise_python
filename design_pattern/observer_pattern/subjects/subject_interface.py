from abc import ABC, abstractmethod
from observer import IObserver

class ISubject(ABC):

    def __init__(self):
        self.observers=[]

    @abstractmethod
    def attach(self,observer: IObserver): 
        pass

    def detach(self,observer: IObserver):
        pass

    def notify(self, absence:str, designee:str):
        pass