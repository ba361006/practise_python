# -*- coding: utf-8 -*-
import platform
import time

import pyperclip
from pynput import keyboard
from PySide6 import QtCore
from PySide6 import QtWidgets


class Worker(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.key = "<ctrl>+q"

    def run_method(self):
        def for_canonical(hotkey_event):
            return lambda key: hotkey_event(self.listener.canonical(key))

        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse(self.key), self.__get_text_from_clipboard
        )
        self.listener = keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release),
        )
        self.listener.start()

    def __get_text_from_clipboard(self) -> str:
        # delay is needed before getting str from clip
        if platform.system() == "Windows":
            modifier = keyboard.Key.ctrl
        elif platform.system() == "Darwin":
            modifier = keyboard.Key.cmd
        controller = keyboard.Controller()
        controller.press("<ctrl>")
        controller.press("c")
        controller.release("c")
        controller.release(modifier)
        time.sleep(0.05)
        print("pyperclip.paste().strip(): ", pyperclip.paste().strip())
        return pyperclip.paste().strip()


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def build(self):
        self.__worker = Worker()

        self.button = QtWidgets.QPushButton()
        self.button.clicked.connect(self.button_pressed)
        self.setCentralWidget(self.button)
        self.show()

    def button_pressed(self):
        self.__thread_crawler_worker = QtCore.QThread()
        self.__thread_crawler_worker.setObjectName("thread_crawler_worker")
        self.__worker.moveToThread(self.__thread_crawler_worker)
        self.__thread_crawler_worker.started.connect(  # type: ignore
            self.__worker.run_method
        )
        self.__thread_crawler_worker.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = Main()
    main.build()
    app.exec()
