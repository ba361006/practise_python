# -*- coding: utf-8 -*-
import platform
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMenu
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


def add_menu(mainWindow):
    if platform.system() == "Darwin":
        mainWindow.menuBar = MenuBar()
        mainWindow.centralWidget().layout().addWidget(mainWindow.menuBar)


class MenuBar(QMenu):
    """Menu bar that displays the open windows on MacOS"""

    menu_items = {}

    def __init__(self):
        super().__init__()
        self.setAsDockMenu()
        self.hide()

    def add_window(self, window, title):
        show_action = self.addAction(title)
        show_action.triggered.connect(window.showNormal)
        self.menu_items[title] = show_action
        return

    def remove_window(self, title):
        show_action = self.menu_items.pop[title]
        self.removeAction(show_action)
        return


class Window(QWidget):
    def __init__(self, title, windows, dockMenu):
        super().__init__()

        self.title = title
        self.windows = windows
        self.dockMenu = dockMenu
        self.setWindowTitle(title)
        self.show()

    def closeEvent(self, event):
        self.windows.pop(self.title)

        if platform.system() == "Darwin":
            self.dockMenu.remove_window(self.title)

        event.accept()
        self.destroy()


class MainWindow(QMainWindow):
    windows = {}

    def __init__(self):
        super().__init__()

        self.setCentralWidget(QWidget())
        c_widget = self.centralWidget()
        c_widget.setLayout(QVBoxLayout())

        # If using MacOS, create a menubar to view windows.
        add_menu(self)

        add_item = QPushButton("Add")
        add_item.clicked.connect(self.add_window)
        c_widget.layout().addWidget(add_item)

        print_window = QPushButton("Print Windows")
        print_window.clicked.connect(self.show_windows)
        c_widget.layout().addWidget(print_window)

        self.show()

    def add_window(self):
        title = str(len(self.windows.keys()))
        self.window = Window(title, self.windows, self.menuBar)
        self.windows[title] = self.window

        self.menuBar.add_window(self.window, title)

    def show_windows(self):
        print(self.windows.keys())

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
