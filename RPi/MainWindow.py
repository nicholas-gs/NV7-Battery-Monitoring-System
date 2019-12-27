import sys
import time

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from threading import Event

from MainWindow_ui import Ui_MainWindow
from SerialHelper import ComPort


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.comPort = ComPort()
        self.comPort.newValue.connect(self.updateUI)
        self.comPort.start()

    # Update the UI with the new temperature data
    def updateUI(self, moduleID,  tempData):
        self.displayData(moduleID, tempData, self.calculateAvg(tempData))

    def displayData(self, moduleID, tempData, tempAverage):
        if(moduleID == 0):
            self._displayMod0Data(tempData, tempAverage)
        elif(moduleID == 1):
            self._displayMod1Data(tempData, tempAverage)
        elif(moduleID == 2):
            self._displayMod2Data(tempData, tempAverage)
        elif(moduleID == 3):
            self._displayMod3Data(tempData, tempAverage)
        elif(moduleID == 4):
            self._displayMod4Data(tempData, tempAverage)
        elif(moduleID == 5):
            self._displayMod5Data(tempData, tempAverage)

    # Calculate the average temp
    def calculateAvg(self, tempData):
        i = 0
        sum = 0

        for temp in tempData:
            if(temp != -1):
                sum += temp
                i += 1

        if(i == 0):
            return -1
        else:
            return ((int)(sum/i))
