import sys
from PyQt5 import QtCore, QtWidgets


class Window_4(QtWidgets.QWidget):
    
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('User_Guide_Page')
        self.setGeometry(100, 100, 600, 400)

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Home_Page')
        self.button.clicked.connect(self.back_to_window_1)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def back_to_window_1(self):
        self.close()
        self.switch_window.emit()


class Window_3(QtWidgets.QWidget):

    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Prediction')
        self.setGeometry(100, 100, 600, 400)

        layout = QtWidgets.QGridLayout()

        self.button1 = QtWidgets.QPushButton('User_Guide_Page')
        self.button1.clicked.connect(self.goto_page_4)
        layout.addWidget(self.button1)

        self.button2 = QtWidgets.QPushButton('Home_Page')
        self.button2.clicked.connect(self.goto_page_1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def goto_page_4(self):
        self.close()
        self.switch_window1.emit()
    def goto_page_1(self):
        self.close()
        self.switch_window2.emit()

class Window_2(QtWidgets.QWidget):

    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Analysis')
        self.setGeometry(100, 100, 600, 400)

        layout = QtWidgets.QGridLayout()

        self.button1 = QtWidgets.QPushButton('User_Guide_Page')
        self.button1.clicked.connect(self.user_guide_page)
        layout.addWidget(self.button1)

        self.button2 = QtWidgets.QPushButton('Home_Page')
        self.button2.clicked.connect(self.goto_page_1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def user_guide_page(self):
        self.close()
        self.switch_window1.emit()
    def goto_page_1(self):
        self.close()
        self.switch_window2.emit()

class Window_1(QtWidgets.QWidget):

    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Home_Page')
        self.setGeometry(100, 100, 600, 400)

        layout = QtWidgets.QGridLayout()

        self.button1 = QtWidgets.QPushButton('Analysis')
        self.button1.clicked.connect(self.goto_page_2)
        layout.addWidget(self.button1)

        self.button2 = QtWidgets.QPushButton('Prediction')
        self.button2.clicked.connect(self.goto_page_3)
        layout.addWidget(self.button2)

        self.button3 = QtWidgets.QPushButton('User_Guide_Page')
        self.button3.clicked.connect(self.goto_page_4)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def goto_page_2(self):
        self.switch_window1.emit()
    def goto_page_3(self):
        self.close()
        self.switch_window2.emit()
    def goto_page_4(self):
        self.close()
        self.switch_window3.emit()


class Controller:

    def __init__(self):
        pass

    def show_window_1(self):
        self.window_1 = Window_1()
        self.window_1.switch_window1.connect(self.show_window_2)
        self.window_1.switch_window2.connect(self.show_window_3)
        self.window_1.switch_window3.connect(self.show_window_4)
        self.window_1.show()

    def show_window_2(self):
        self.window_2 = Window_2()
        self.window_2.switch_window1.connect(self.show_window_4)
        self.window_2.switch_window2.connect(self.show_window_1)
        self.window_1.close()
        self.window_2.show()

    def show_window_3(self):
        self.window_3 = Window_3()
        self.window_3.switch_window1.connect(self.show_window_4)
        self.window_3.switch_window2.connect(self.show_window_1)
        self.window_3.show()

    def show_window_4(self):
        self.window_4 = Window_4()
        self.window_4.switch_window.connect(self.show_window_1)
        #self.window_2.close()
        self.window_4.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_window_1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()