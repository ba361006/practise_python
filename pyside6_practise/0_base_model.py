# -*- coding: utf-8 -*-
import os
import sys
import time

import pyperclip
from pynput import keyboard
from PySide6 import QtCore
from PySide6 import QtWidgets


class Main(QtWidgets.QMainWindow):
    signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.set_central_widget()

    def set_central_widget(self):
        self.central_widget = QtWidgets.QWidget()
        self.central_layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def build(self):
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName("Hello")
    app.setApplicationName("app")
    main = Main()
    main.build()
    app.exec()
