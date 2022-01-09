from . import furniture_factory
import furniture

class ClassicFactory(furniture_factory.FurnitureFactory):
    def createChair(self):
        return furniture.ClassicChair()

    def createTable(self):
        return furniture.ClassicTable()