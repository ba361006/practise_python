# -*- coding: utf-8 -*-
import time

import pyperclip
from pynput import keyboard


def get_text_from_clip():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.cmd)
    controller.press("c")
    controller.release("c")
    controller.release(keyboard.Key.cmd)
    time.sleep(0.05)
    print(pyperclip.paste().strip())


def for_canonical(hotkey_event):
    return lambda key: hotkey_event(listener.canonical(key))


hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+q"), get_text_from_clip)
with keyboard.Listener(
    on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)
) as listener:
    listener.join()
