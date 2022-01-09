from . import vehicle_interface

class Truck(vehicle_interface.IVehicle):
    def deliver(self):
        print("deliver by truck")