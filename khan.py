from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import sys
import time


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('/home/pi/KLGlass/UI/demo.ui', self)
        # self.Gio1 = self.findChild(QtWidgets.QLabel, 'Gio1')  # Find the button
        # Remember to pass the definition/method, not the return value!
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showMaximized()
        self.show()

    def loadding(self):
        print('printButtonPressed')
        # self.Gio1.setText('khan')
        # self.Gio1.setText(str(i))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.loadding()
app.exec_()
