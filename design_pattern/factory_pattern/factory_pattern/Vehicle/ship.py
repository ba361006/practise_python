from . import vehicle_interface

class Ship(vehicle_interface.IVehicle):
    def deliver(self):
        print("deliver by ship")