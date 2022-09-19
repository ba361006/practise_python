from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
  

class ComboCheckBox(QComboBox):
    def __init__(self, items: list):
        """
        initial function
        :param items: the items of the list
        """
        super(ComboCheckBox, self).__init__()
        self.items = items  # items list
        self.box_list = []  # selected items
        self.text = QLineEdit()  # use to select items
        self.text.setReadOnly(True)

        # every checkbox should be seen as a single object, so you can use a
        # list and append many of it
        q = QListWidget()
        for i in range(len(self.items)):
            self.box_list.append(QCheckBox())
            self.box_list[i].setText(self.items[i])
            item = QListWidgetItem(q)
            q.setItemWidget(item, self.box_list[i])
            self.box_list[i].stateChanged.connect(self.show_selected)

        # the text show on the combobox
        self.setLineEdit(self.text)

        # just set it, otherwise programme can be run
        self.setModel(q.model())
        self.setView(q)

    def get_selected(self) -> list:
        """
        get selected items
        :return:
        """
        ret = []
        for i in range(len(self.items)):
            if self.box_list[i].isChecked():
                ret.append(self.box_list[i].text())
        return ret

    def show_selected(self):
        """
        show selected items
        :return:
        """
        self.text.clear()
        ret = '; '.join(self.get_selected())
        self.text.setText(ret)

# create pyqt5 app 
App = QApplication(sys.argv) 

# create the instance of our Window 
combobox = ComboCheckBox(["hello", "hello!"])
combobox.show()

# start the app 
sys.exit(App.exec()) 