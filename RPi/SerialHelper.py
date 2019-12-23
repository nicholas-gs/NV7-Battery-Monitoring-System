from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import  QThread
import datetime,  time
import serial


class ComPort(QThread):

    newValue = pyqtSignal(object , object)
    
    def __init__(self,  event):
        QThread.__init__(self)
        self.stopped = event
        
    def run(self):

        self.ser = None # Com Port object
        while(self.ser == None):
            # ui.serArduino = serial.Serial("/dev/ttyACM0",9600,timeout=1)       #Raspberry Pi
            self.ser = serial.Serial("COM4", 9600)        

        while not self.stopped.wait(0.1):    #1 max 0.3
            self.ArduinoLoop()
    
    def ArduinoLoop(self):
        i = 0
        dataArray = None
        while(True):
            
            # Create a new array
            if(i == 0):
                dataArray = [0] * 32 # Data Array of size 32 elements

            # Read in a byte array from the com port
            line = self.ser.readline().rstrip()


            if(len(line) == 5):
                lineStr = self.convertByteToString(line)
                c = lineStr[3]
                x = int(c)
                dataArray[i] = x
            else:
                print("Invalid data")
            i += 1
            if(i == 31):
                i = 0
                print("Emmiting signal")
                
                self.newValue.emit(i, dataArray)
                
    # Convert byte array into string
    def convertByteToString(self, data):
        return "".join(chr(x) for x in data)
       
          
