from . import observer_interface

class PrivateBranchExchange(observer_interface.IObserver):

    def update(self, absence:str, designee:str):
        print("[PBX] 已指定轉接{0}的來電給{1}!".format(absence, designee))