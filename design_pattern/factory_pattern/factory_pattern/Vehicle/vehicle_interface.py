import abc

class IVehicle(abc.ABC):
    @abc.abstractmethod
    def deliver(self):
        pass