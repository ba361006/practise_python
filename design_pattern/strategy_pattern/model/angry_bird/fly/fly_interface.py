import abc

class IFly(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass