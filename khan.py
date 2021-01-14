from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime, Qt, QDate
import sys
from bluedot.btcomm import BluetoothServer

strLocal = '/home/pi/KLGlass'
strPc = '.'


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(strPc+'/UI/MatChinh.ui', self)
        self.TimeTxt = self.findChild(QtWidgets.QLabel, 'Time')
        self.DateTxt = self.findChild(QtWidgets.QLabel, 'Ngay')
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        def data_received(data):
            print(data)
            self.TimeTxt.setText(data)
            s.send(data)
        s = BluetoothServer(data_received)

    def showTime(self):
        # getting current time
        current_time = QTime.currentTime()
        current_Date = QDate.currentDate()

        label_date = current_Date.toString('dd.MM.yyyy')
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        # showing it to the label
        self.TimeTxt.setText(label_time)
        self.DateTxt.setText(label_date)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.showMaximized()
window.show()
app.exec_()
