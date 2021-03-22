class test:
    def __init__(self, a):
        print("__init__: ", a)
    def __call__ (self,a):
        print("__call__: ", a)

test(1)