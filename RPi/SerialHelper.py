from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import datetime
import time
import serial


class ComPort(QThread):

    newValue = pyqtSignal(object, object)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while(True):
            self.ser = None  # Com Port object
            while(self.ser == None):
                try:
                    # self.serArduino = serial.Serial("/dev/ttyACM0",9600,timeout=1)     # Raspberry Pi
                    self.ser = serial.Serial(
                        "COM3", 9600)                               # PC
                except:
                    print("Cannot find COM Port")

            # When the COM port connection first starts, the first few readings may give invalid reads. So wait until reading is stable
            while(not self.startValidInputs()):
                continue

            while(True):
                try:
                    self.readDataStream()
                except:
                    print("Error reading in data from com port")
                    break  # We break because the exception may be caused of the COM Port connection dropping, so we need to try to connect again

    # Sanity check -- The string from the COM port should be of length 5 or 6
    def startValidInputs(self):
        line = self.ser.readline().rstrip()
        if(len(line) == 5 or len(line) == 6):
            return True
        else:
            return False

    # Continuously read in data stream from the COM port
    def readDataStream(self):
        dataArray = [-1] * 32  # Init Data Array of size 32 elements
        moduleID = -1

        while(True):
            # Read in a byte array from the com port
            line = self.ser.readline().rstrip()
            # String should have 5 or 6 characters
            # 1st char is the module index, 2nd & 3rd char is the thermistor id, 4th,5th. If the string has 6 char, discard the 6th char
            if(len(line) == 5 or len(line) == 6):
                # Convert byte array to string
                lineStr = self.convertByteToString(line)

                y = int(lineStr[0])  # Get module id
                # If the module id for this string is not the same as the current module id, means upcoming data is for another battery module.
                # So pass the existing temp data array to main thread for display
                if(y != moduleID):
                    # Pass data to main thread.
                    self.newValue.emit(moduleID, dataArray)
                    moduleID = y  # Set module id to the new id
                    dataArray = [-1] * 32  # Reset data array

                # Get 2nd and 3rd char (thermistor id)
                sensorID = int(lineStr[1:3])
                c = lineStr[3:5]  # Get 4th and 5th char (temp data)
                x = int(c)       # Convert string to int
                dataArray[sensorID] = x  # Put temp into data array

    # Convert byte array into string
    def convertByteToString(self, data):
        return "".join(chr(x) for x in data)
