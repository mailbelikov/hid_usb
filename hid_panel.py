from hid_usb import Ui_Form
from PyQt5 import QtWidgets as QW
from pywinusb import hid
import sys, time

class my_app(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.IR = hid.HidDeviceFilter(vendor_id = 0x1130, product_id = 0xcc00).get_devices()[0]

        self.ui.pbStart.clicked.connect(self.Start)
        self.ui.pbStop.clicked.connect(self.Stop)

    def Start(self):
        self.IR.open()
        self.IR.set_raw_data_handler(self.IRRead)

    def IRRead(self, data):
        if data[2] > 0:
#            button = f'self.ui.pb{str(data[2]).setEnable(False)'
            eval(f'self.ui.pb{str(data[2])}.setEnabled(False)')
            time.sleep(0.5)
            eval(f'self.ui.pb{str(data[2])}.setEnabled(True)')

    def Stop(self):
        self.IR.close()

app = QW.QApplication(sys.argv)
window = my_app()
window.show()
app.exec_()