# -*- coding: utf-8 -*-
class Grandpa:
    def __init__(self, name: str) -> None:
        print("Grandpa: ", name)
        print("This will instantiate your Mom: ", super().__init__("from Grandpa"))


class Dad(Grandpa):
    def __init__(self, name: str) -> None:
        print("Dad: ", name)
        super().__init__("from Dad")


class Mom:
    def __init__(self, name: str) -> None:
        print("Mom: ", name)


class Child(Dad, Mom):
    def __init__(self) -> None:
        super().__init__("from Child")


print(Child.mro())
child = Child()
