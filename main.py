import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.a = QtWidgets.QWidget(MainWindow)
        self.a.setObjectName("a")

        self.butn = QtWidgets.QPushButton(self.a)
        self.butn.setGeometry(QtCore.QRect(300, 350, 400, 70))

        MainWindow.setCentralWidget(self.a)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 20))
        self.menubar.setObjectName("menubar")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.butn.setFont(font)
        self.butn.setObjectName("butn")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("stat")
        MainWindow.setStatusBar(self.statusbar)

        self.trans(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def trans(self, MainWindow):
        tr = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(tr("MainWindow", "MainWindow"))
        self.butn.setText(tr("MainWindow", "Создать окружность"))


class Example(QMainWindow, MainWindow_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pai = False
        self.butn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.pai:
            circl = QPainter()
            circl.begin(self)
            self.draw(circl)
            circl.end()

    def paint(self):
        self.pai = True
        self.repaint()

    def draw(self, circl):
        b = random.randint(20, 500)
        circl.setBrush(QColor(random.randint(0, 255), random.randint(0, 255),
                              random.randint(0, 255)))
        circl.drawEllipse(random.randint(0, 1000), random.randint(0, 800), b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
