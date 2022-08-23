import enum


class Test:
    def __init__(self):
        print("init")
    
    def __call__(self):
        print("call")


Test()