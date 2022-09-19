import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   win = QWidget()
   button1 = QPushButton(win)
   button1.setText("Show dialog!")
   button1.move(50,50)
   button1.clicked.connect(showDialog)
   win.setWindowTitle("Click button")
   win.show()

   # So for PyQt5 with Python 3, exec_() and exec() are the same. 
   # For older PyQt, only exec_() is available.
   sys.exit(app.exec_())
	
def showDialog():
   # note that the return value from QMessageBox.information or msgBox.exec() are different
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Message box pop up window")
   msgBox.setWindowTitle("QMessageBox Example")
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msgBox.buttonClicked.connect(msgButtonClick)

   # exec() means start the programme, and wait until the corresponding dialog is closed
   # then return the value (QMessageBox.ok or QMessageBox.Cancel in this example)
   returnValue = msgBox.exec()
   print(f"QMessageBox.Ok: {QMessageBox.Ok}, QMessageBox.Cancel: {QMessageBox.Cancel}, returnValue:{returnValue}")
   
def msgButtonClick(i):
   print("Button clicked is:",i.text())
	
if __name__ == '__main__': 
   window()