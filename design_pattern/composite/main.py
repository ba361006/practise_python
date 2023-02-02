# -*- coding: utf-8 -*-
class Component:
    def __init__(self, name):
        self._name = name

    def operation(self):
        pass

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def get_child(self, index):
        pass


class Leaf(Component):
    def operation(self):
        print(f"Leaf {self._name} operation")

    def add(self, component):
        print("Cannot add to a leaf")

    def remove(self, component):
        print("Cannot remove from a leaf")

    def get_child(self, index):
        print("Leaf has no children")
        return None


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def operation(self):
        print(f"Composite {self._name} operation")
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def get_child(self, index):
        return self._children[index]


# Example usage
root = Composite("root")
leaf1 = Leaf("leaf1")
leaf2 = Leaf("leaf2")
root.add(leaf1)
root.add(leaf2)
root.operation()
