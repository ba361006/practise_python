from . import furniture_factory
import furniture

class ModernFactory(furniture_factory.FurnitureFactory):
    def createChair(self):
        return furniture.ModernChair()

    def createTable(self):
        return furniture.ModernTable()