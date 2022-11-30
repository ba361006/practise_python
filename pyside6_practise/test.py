# -*- coding: utf-8 -*-
import os
import sys
import time

import pyperclip
from pynput import keyboard
from PySide6 import QtCore
from PySide6 import QtWidgets


class Main(QtWidgets.QMainWindow):
    signal = QtCore.Signal(bool)

    def __init__(self):
        super().__init__()
        self.set_central_widget()

    def set_central_widget(self):
        self.central_widget = QtWidgets.QWidget()
        self.central_layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def build(self):
        self.signal.connect(self.hello)
        check_box = QtWidgets.QCheckBox()
        button = QtWidgets.QPushButton()
        button.clicked.connect(lambda: self.signal.emit("true"))
        self.central_layout.addWidget(button)
        self.central_layout.addWidget(check_box)
        self.show()

    def hello(self, a):
        print("hello: ", a)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = Main()
    main.build()
    app.exec()
