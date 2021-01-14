from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime, Qt, QDate
import sys
#from bluedot.btcomm import BluetoothServer

strLocal = '/home/pi/KLGlass'
strPc = '.'
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime, Qt, QDate
import sys
from bluedot.btcomm import BluetoothServer
from gpiozero import LED, Button

strLocal = '/home/pi/KLGlass'
strPc = '.'


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(strLocal+'/UI/MatChinh.ui', self)
        self.TimeTxt = self.findChild(QtWidgets.QLabel, 'Time')
        self.DateTxt = self.findChild(QtWidgets.QLabel, 'Ngay')
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.btn_count =0
        self.led_status = 0
        self.led = LED("GPIO17")
        self.cutRun = LED("GPIO26")
        self.screen_btn = Button("BOARD7")
        clock_time = QTimer(self)
        clock_time.timeout.connect(self.actions)
        clock_time.start(100)

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
    def actions(self):
        print(self.btn_count)
        if self.btn_count < 20: 
          self.btn_count = self.btn_count + 1

        if not self.screen_btn.is_pressed:
          if self.led_status == 0 and self.btn_count < 3:
             self.led_status = 1
             self.led.on()
          elif self.led_status == 1 and self.btn_count < 3:
             self.led_status = 0
             self.led.off()
          self.btn_count = 0  
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.showMaximized()
window.show()
app.exec_()
