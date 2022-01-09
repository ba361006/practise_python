from . import fly_interface

class SlowFly(fly_interface.IFly):
    def fly(self):
        print("fly slowly")

class FastFly(fly_interface.IFly):
    def fly(self):
        print("fly quickly")