from . import observer_interface

class MailServer(observer_interface.IObserver):

    def update(self, absence:str, designee:str):
        print("[Mail Server] 已設定將{0}的信副本給{1}!".format(absence, designee))