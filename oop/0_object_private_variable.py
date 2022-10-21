class Math:
    __offset = 100

    def readOffset(self):
        print("the Math function offset has returned")
        return self.__offset


class Calculator(Math):
    def addValue(self, a, b):
        self.__offset = 20
        print("the object is %s, __offset at %s" % (self, self.__offset))
        return a + b + self.readOffset()


m = Calculator()
print(m.addValue(20, 30))
