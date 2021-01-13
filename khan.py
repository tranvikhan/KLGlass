from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import sys
from bluedot.btcomm import BluetoothServer
from signal import pause

strLocal = '/home/pi/KLGlass'
strPc = '.'


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(strLocal+'/UI/MatChinh.ui', self)
        self.SpeedText = self.findChild(
            QtWidgets.QLabel, 'Speed')  # Find the button
        # Remember to pass the definition/method, not the return value!
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.showMaximized()
        self.show()

    def loadding(self, str):
        self.SpeedText.setText(str)


app = QtWidgets.QApplication(sys.argv)
window = Ui()


def data_received(data):
    print(data)
    window.loadding(data)
    s.send(data)


s = BluetoothServer(data_received)
pause()
app.exec_()
