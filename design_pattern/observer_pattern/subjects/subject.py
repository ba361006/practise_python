from . import subject_interface
import observer

class Subject(subject_interface.ISubject):
    def __init__(self):
        super().__init__()

    def attach(self,observer: observer.IObserver): 
        self.observers.append(observer)

    def detach(self,observer: observer.IObserver):
        self.observers.remove(observer)

    def notify(self, absence:str, designee:str):
        for observer in self.observers:
            observer.update(absence, designee)