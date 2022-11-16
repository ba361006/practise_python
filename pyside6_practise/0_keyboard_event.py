# -*- coding: utf-8 -*-
import os
import plistlib
import random
import string
import sys
import threading
import time

import pyperclip
from pynput import keyboard
from PySide6 import QtCore
from PySide6 import QtWidgets


class Main(QtWidgets.QMainWindow):
    signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

    def build(self):
        # self.create_plist()
        self.signal.connect(self.get_text_from_clip)
        self.button = QtWidgets.QPushButton()
        self.button.clicked.connect(self.button_pressed)
        self.keyboard_detect_start()
        self.setCentralWidget(self.button)
        self.show()

    def create_plist(self):
        app_path = os.path.splitext(sys.argv[0])[0]
        startup_folder = os.environ["HOME"] + "/Library/LaunchAgents/"
        plist = {
            "Label": "autocambridge",
            "ProgramArguments": [f"{app_path}"],
            "LimitLoadToSessionType": "Aqua",
            "RunAtLoad": True,
            "StandardErrorPath": "/dev/null",
            "StandardOutPath": "/dev/null",
        }
        plistlib.dump(plist, open(startup_folder + "autocambridge.plist", "wb+"))

    def keyboard_detect_start(self, key="<ctrl>+q"):
        def for_canonical(hotkey_event):
            return lambda key: hotkey_event(self.listener.canonical(key))

        hotkey = keyboard.HotKey(keyboard.HotKey.parse(key), self.signal.emit)
        print("hotkey")
        self.listener = keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release),
        )
        self.listener.start()
        print("start")

    def get_text_from_clip(self):
        controller = keyboard.Controller()
        controller.press(keyboard.Key.cmd)
        controller.press("c")
        controller.release("c")
        controller.release(keyboard.Key.cmd)
        time.sleep(0.05)
        print(pyperclip.paste().strip())

    def button_pressed(self):
        self.listener.stop()
        self.listener.join()
        # new_key = random.choices(string.ascii_lowercase)[0]
        # print("new_key: ", new_key)
        # self.keyboard_detect_start(key=f"<ctrl>+{new_key}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = Main()
    main.build()
    app.exec()
