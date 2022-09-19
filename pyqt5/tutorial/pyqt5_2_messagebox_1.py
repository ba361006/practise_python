from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
  
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setGeometry(100,100,40,20)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)
 
    def msg(self):
        # easy way to pop out the message box
        reply = QMessageBox.information(self, "标题", "消息", QMessageBox.Yes | QMessageBox.No)
        print("Get replay: ",reply)
                                    

if __name__=="__main__":  
    import sys
    app=QtWidgets.QApplication(sys.argv) 
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())