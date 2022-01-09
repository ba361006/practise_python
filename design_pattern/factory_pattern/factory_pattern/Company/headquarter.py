import abc

# Headquarter asks every subsidiary should have it own deliver method
# and should be able to deliver
class Headquarter(abc.ABC):
    def __init__(self):
        self.Subsidiary = self.deliverMethod()

    @abc.abstractmethod
    def deliverMethod(self):
        pass
    
    def startDeliver(self):
        self.Subsidiary.deliver()