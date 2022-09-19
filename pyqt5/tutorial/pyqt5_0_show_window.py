import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    # initalize QApplication
    app = QApplication(sys.argv)

    # QWidget is the fundamental element in pyqt5
    Window = QWidget()

    # resize width = 250, height = 150
    Window.resize(250, 150)

    # move to [300, 300]([x,y]) on our screen, initial point is on the upper-left
    Window.move(300, 300)

    # set title
    Window.setWindowTitle('Window')

    # show
    Window.show()

    # exit
    sys.exit(app.exec_())