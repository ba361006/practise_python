from . import chair

class ClassicChair(chair.Chair):
    def sitOn(self):
        return "Client sits on a classic chair"