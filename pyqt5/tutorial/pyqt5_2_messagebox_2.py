import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 166)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("YaHei Consolas Hybrid")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "對話框"))
        self.pushButton.setText(_translate("Form", "彈出對話框"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMsg)

    def showMsg(self):
        information = QMessageBox.information(self, '提示對話框','提示對話框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        question = QMessageBox.question(self, "提問對話框", "提問對話框", QMessageBox.Yes | QMessageBox.No)
        warning = QMessageBox.warning(self, "警告對話框", "警告對話框", QMessageBox.Yes | QMessageBox.No)
        critical = QMessageBox.critical(self, "嚴重錯誤對話框", "嚴重錯誤對話框", QMessageBox.Yes | QMessageBox.No,)
        about = QMessageBox.about(self, "關於對話框", "關於對話框")
        print(f"information: {information}, question: {question}, warning: {warning}, critical: {critical}, about: {about}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())