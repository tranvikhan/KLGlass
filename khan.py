from PyQt5 import QtWidgets, uic
import sys
import time


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./UI/GlaasFace1.ui', self)
        self.Gio1 = self.findChild(QtWidgets.QLabel, 'Gio1')  # Find the button
        # Remember to pass the definition/method, not the return value!
        i = 0

        self.show()

    def loadding(self):
        while 1:
            print('printButtonPressed')
            # self.Gio1.setText(str(i))
            time.sleep(3)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
