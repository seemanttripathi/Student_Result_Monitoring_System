import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QCursor
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap,QFont,QIcon

headfont = QFont("Yu Gothic UI Light",48)
smallfont = QFont("Segoe Print",14)
smallfont2 = QFont("Segoe Script",18)

class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)

       self.setWindowTitle("SRMS - Student Result Monitoring System !!")
       self.setWindowIcon(QIcon("Images/hist.png"))

       width = 960
       height = 630
       self.setMinimumSize(width, height)
       self.setGeometry(100,100,300,200)

       oImage = QImage("solar_system.png")
       sImage = oImage.scaled(QSize(1700,1000))
       palette = QPalette()
       
       palette.setBrush(QPalette.Window, QBrush(sImage))                        
       self.setPalette(palette)


       vlayout = QtWidgets.QVBoxLayout()
       #hlayout = QtWidgets.QHBoxLayout()
       #grid = QGridLayout()
       #grid.setSpacing(10)


       vlayout.addStretch(2)
       self.text1=QLabel("Let's get started!",self)
       self.text1.setFont(headfont)
       #grid.addWidget(self.text1,0,0)
       #self.text1.move(150,150)
       vlayout.addWidget(self.text1)

       

       self.text2=QLabel("explore visualization and improve your analysis",self)
       self.text2.setFont(smallfont)
       vlayout.addWidget(self.text2)
       vlayout.addStretch(1)

       
       css = """
            border-radius: 5px;
            border: 1px solid blue;
            font-size: 30px;
            padding: 10px;
            margin: 5px;
            background-color: #FCF9F9;
            Layout.fillWidth: true;   
            """
        
       self.analysis=QPushButton("Start Analysis...",self)
       self.analysis.setFont(smallfont)
       self.analysis.setStyleSheet(css)
       vlayout.addWidget(self.analysis)
       self.analysis.setFixedWidth(500)
       self.analysis.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
       self.analysis.clicked.connect(self.messageBox)


       self.prediction=QPushButton("Start Prediction...",self)
       self.prediction.setFont(smallfont)
       self.prediction.setStyleSheet(css)
       vlayout.addWidget(self.prediction)
       self.prediction.setFixedWidth(500)
       self.prediction.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


       self.unknown=QPushButton("Show User Guides...",self)
       self.unknown.setFont(smallfont)
       self.unknown.setStyleSheet(css)
       vlayout.addWidget(self.unknown)
       self.unknown.setFixedWidth(500)
       self.unknown.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

       #vlayout.fillWidth: true;
       vlayout.addStretch(3)


       self.setLayout(vlayout)
       self.showMaximized()
       self.show()       
       #self.setLayout(hlayout)
       #self.text1.move(85,100)

    def messageBox(self):
        mbox=QMessageBox.question(self,"Warning","Are you sure to EXIT..??",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Yes)
        if mbox==QMessageBox.Yes:
            sys.exit()
        elif mbox==QMessageBox.No or mbox==QMessageBox.Cancel:
            #Do Nothing
            pass


if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())