from . import headquarter
import Vehicle

class RoadSubsidiary(headquarter.Headquarter):
    def deliverMethod(self):
        return Vehicle.Truck()
