import sys
import time

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from threading import Event

from MainWindow_ui import Ui_MainWindow
from SerialHelper import ComPort
from ui_elements import TempSensors


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.comPort = ComPort()
        self.msgBox = None  # Message box that is displayed when error occurs
        self.comPort.newValue.connect(self.updateUI)
        self.comPort.statusEvent.connect(self.displayMessageBox)
        self.comPort.start()

    # Update the UI with the new temperature data
    def updateUI(self, moduleID,  tempData):
        # Send array for adjustment
        self.adjustTemps(moduleID, tempData)
        # Calculate average temperature for module
        avg = self.calculateAvg(moduleID, tempData)
        self.displayData(moduleID, tempData, avg)

    # Update the temperature based on moduleID -- 0,1,2,4,5,6
    def displayData(self, moduleID, tempData, tempAverage):
        if(moduleID == 0):
            self._displayMod0Data(tempData, tempAverage)
        elif(moduleID == 1):
            self._displayMod1Data(tempData, tempAverage)
        elif(moduleID == 2):
            self._displayMod2Data(tempData, tempAverage)
        elif(moduleID == 4):
            self._displayMod3Data(tempData, tempAverage)
        elif(moduleID == 5):
            self._displayMod4Data(tempData, tempAverage)
        elif(moduleID == 6):
            self._displayMod5Data(tempData, tempAverage)

    # Adjust original temperature reading with the offsets
    def adjustTemps(self, moduleID, tempData):
        i = 0
        for temp in tempData:
            if(temp != -1):           # Don't do adjustment for temperature if it is -1 (default invalid value)
                tempData[i] = temp - TempSensors.sensorOffsets[moduleID][i]
            i += 1

    # Calculate the average temp from the array of temperature readings for a single module
    def calculateAvg(self, moduleID, tempData):
        i = 0  # Number of valid temperatures
        counter = 0
        sum = 0

        for temp in tempData:
            if(temp != -1):
                sum += temp
                i += 1
            counter += 1

        if(i == 0):
            return -1
        else:
            return ((int)(sum/i))

    # Program status passed from the background SerialHelper thread.
    # If True -- Error, else no error
    def displayMessageBox(self, isError, msg):
        if(isError and self.msgBox is None):
            self.msgBox = QMessageBox()
            self.msgBox.setWindowTitle("Program status")
            self.msgBox.setText(msg)    # Display error message on MessageBox
            self.msgBox.show()
        elif(not isError and self.msgBox is not None):
            print("Closing box")
            self.msgBox.close()         # Hide MessageBox
            self.msgBox = None
