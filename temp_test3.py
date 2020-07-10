import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QCursor
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap,QFont,QIcon



headfont = QFont("Yu Gothic UI Light",48)
smallfont = QFont("Segoe Print",14)
smallfont2 = QFont("Segoe Script",18)


class TitleBar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        css = """
        QWidget{
            Background: #696969;
            color: white;
            font: 22px bold;
            font-weight: ;
            border-radius: 1px;
        }
        QDialog{
            Background-image:url('Images/hist.png');
            font-size:10px;            
            color: black;

        }
        QToolButton{
            Background: #696969;
            font-size: 11px;
        }
        QToolButton:hover{
            Background: blue;
            font-size: 11px;
        }
        """

        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)
        self.minimize=QtWidgets.QToolButton(self)
        self.minimize.setIcon(QtGui.QIcon('Images/minimize_btn2.png'))
        self.maximize=QtWidgets.QToolButton(self)
        self.maximize.setIcon(QtGui.QIcon('Images/maximize_btn.png'))
        close=QtWidgets.QToolButton(self)
        close.setIcon(QtGui.QIcon('Images/exit_close_btn3.png'))

        
        h = 45
        w = 70
        self.minimize.setMinimumHeight(h)
        self.minimize.setMinimumWidth(w)
        close.setMinimumHeight(h)
        close.setMinimumWidth(w)
        self.maximize.setMinimumHeight(h)
        self.maximize.setMinimumWidth(w)

        
        label=QtWidgets.QLabel(self)
        label.setText("SRMS - Student Result Monitoring System !!")
        self.setWindowTitle("SRMS - Student Result Monitoring System !!")
        hbox=QtWidgets.QHBoxLayout(self)
        hbox.addStretch(1)
        hbox.addWidget(label)
        hbox.addStretch(6)

        hbox.addWidget(self.minimize)
        hbox.addWidget(self.maximize)
        hbox.addWidget(close)
        
        hbox.insertStretch(1,10)
        hbox.setSpacing(0)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed)
        self.maxNormal=False


        close.clicked.connect(self.close)
        self.minimize.clicked.connect(self.showSmall)
        self.maximize.clicked.connect(self.showMaxRestore)

        hbox.setContentsMargins(0, 0, 0, 0)

    def showSmall(self):
        box.showMinimized()

    def showMaxRestore(self):
        if(self.maxNormal):
            box.showNormal()
            self.maxNormal= False
            self.maximize.setIcon(QtGui.QIcon('Images/maximize_btn.png'))
        else:
            box.showMaximized()
            self.maxNormal=  True
            self.maximize.setIcon(QtGui.QIcon('Images/maximize_btn.png'))

    def close(self):
        box.close()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            box.moving = True
            box.offset = event.pos()

    def mouseMoveEvent(self,event):
        if box.moving: box.move(event.globalPos()-box.offset)


class Frame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.m_mouse_down= False
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        css = """
        QFrame{
            Background:  white;
            color:black;
            font:33px ;
            font-weight:bold;
            }
        """

        width = 960
        height = 630
        self.setMinimumSize(width, height)
        self.setGeometry(100,100,300,200)
        self.showMaximized()
        # width = 960
        # height = 630
        # self.setMinimumSize(width, height)
        # self.setGeometry(100,100,300,200)

        # oImage = QImage("solar_system.png")
        # sImage = oImage.scaled(QSize(1700,1000))
        # palette = QPalette()
       
        # palette.setBrush(QPalette.Window, QBrush(sImage))                        
        # self.setPalette(palette)


        # vlayout = QtWidgets.QVBoxLayout()
        # #hlayout = QtWidgets.QHBoxLayout()
        # #grid = QGridLayout()
        # #grid.setSpacing(10)


        # vlayout.addStretch(2)
        # self.text1=QLabel("Let's get started!",self)
        # self.text1.setFont(headfont)
        # #grid.addWidget(self.text1,0,0)
        # #self.text1.move(150,150)
        # vlayout.addWidget(self.text1)

       

        # self.text2=QLabel("explore visualization and improve your analysis",self)
        # self.text2.setFont(smallfont)
        # vlayout.addWidget(self.text2)
        # vlayout.addStretch(1)

       
        # css = """
        #     border-radius: 5px;
        #     border: 1px solid blue;
        #     font-size: 30px;
        #     padding: 10px;
        #     margin: 5px;
        #     background-color: #FCF9F9;
        #     Layout.fillWidth: true;   
        #     """
        
        # self.analysis=QPushButton("Start Analysis...",self)
        # self.analysis.setFont(smallfont)
        # self.analysis.setStyleSheet(css)
        # vlayout.addWidget(self.analysis)
        # self.analysis.setFixedWidth(500)
        # self.analysis.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # self.analysis.clicked.connect(self.messageBox)


        # self.prediction=QPushButton("Start Prediction...",self)
        # self.prediction.setFont(smallfont)
        # self.prediction.setStyleSheet(css)
        # vlayout.addWidget(self.prediction)
        # self.prediction.setFixedWidth(500)
        # self.prediction.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


        # self.unknown=QPushButton("Show User Guides...",self)
        # self.unknown.setFont(smallfont)
        # self.unknown.setStyleSheet(css)
        # vlayout.addWidget(self.unknown)
        # self.unknown.setFixedWidth(500)
        # self.unknown.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # #vlayout.fillWidth: true;
        # vlayout.addStretch(3)


        # self.setLayout(vlayout)
        # self.showMaximized()
        # self.show()       
        # #self.setLayout(hlayout)
        # #self.text1.move(85,100)

    

        self.setStyleSheet(css)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.m_titleBar= TitleBar(self)
        self.m_content= QtWidgets.QWidget(self)
        vbox=QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.m_titleBar)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.m_content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        vbox.addLayout(layout)
        # Allows you to access the content area of the frame
        # where widgets and layouts can be added
    def messageBox(self):
        mbox=QMessageBox.question(self,"Warning","Are you sure to EXIT..??",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Yes)
        if mbox==QMessageBox.Yes:
            sys.exit()
        elif mbox==QMessageBox.No or mbox==QMessageBox.Cancel:
            #Do Nothing
            pass

    def contentWidget(self):
        return self.m_content

    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self,event):
        self.m_old_pos = event.pos()
        self.m_mouse_down = event.button()== Qt.LeftButton

    def mouseMoveEvent(self,event):
        x=event.x()
        y=event.y()

    def mouseReleaseEvent(self,event):
        m_mouse_down=False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    box = Frame()
    l=QtWidgets.QVBoxLayout(box.contentWidget())
    l.setContentsMargins(0, 0, 0, 0)
    box.show()
    app.exec_()