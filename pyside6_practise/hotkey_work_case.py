# -*- coding: utf-8 -*-
import platform
import time

import pyperclip
from pynput import keyboard
from PySide6 import QtCore
from PySide6 import QtWidgets


class Worker(QtCore.QObject):
    signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.signal.connect(self.print_text_from_clipboard)

    def run_method(self):
        activate_key = "<ctrl>+e"

        def for_canonical(hotkey_event):
            return lambda key: hotkey_event(self.listener.canonical(key))

        hotkey = keyboard.HotKey(keyboard.HotKey.parse(activate_key), self.signal.emit)
        print(hotkey.press.__class__)
        self.listener = keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release),
        )
        self.listener.start()

    def print_text_from_clipboard(self):
        # delay is needed before getting str from clip
        if platform.system() == "Windows":
            modifier = keyboard.Key.ctrl
        elif platform.system() == "Darwin":
            modifier = keyboard.Key.cmd
        controller = keyboard.Controller()
        controller.press(modifier)
        controller.press("c")
        controller.release("c")
        controller.release(modifier)
        time.sleep(0.05)
        print("text: ", pyperclip.paste().strip())


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def build(self):
        self.worker = Worker()

        self.button = QtWidgets.QPushButton()
        self.button.clicked.connect(self.button_pressed)
        self.setCentralWidget(self.button)
        self.show()

    def button_pressed(self):
        self.worker.run_method()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = Main()
    main.build()
    app.exec()
