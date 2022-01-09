from . import headquarter
import Vehicle

class SeaSubsidiary(headquarter.Headquarter):
    def deliverMethod(self):
        return Vehicle.Ship()