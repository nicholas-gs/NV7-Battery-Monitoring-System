import sys
import time

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import  Qt
from threading import Event

from MainWindow_ui import Ui_MainWindow
from SerialHelper import ComPort
        
class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.stop_flag_time =  Event()
        self.stop_flag_RS232 =  Event()

        self.comPort = ComPort(self.stop_flag_RS232)
        self.comPort.newValue.connect(self.updateUI)     
        self.comPort.start() 

    # Update the UI with the new temperature data
    def updateUI(self, moduleID,  tempData):
        self.seg1_100.display(tempData[0])
        self.seg1_101.display(tempData[1])
        
