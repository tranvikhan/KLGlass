from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import sys
from bluedot.btcomm import BluetoothServer

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

        def data_received(data):
            print(data)
            self.SpeedText.setText(data)
            s.send(data)
        s = BluetoothServer(data_received)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
