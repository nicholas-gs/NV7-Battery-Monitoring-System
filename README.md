# NV7 Battery Monitoring System

__Monitor the thermistor array of the NV7 vehicle battery pack__

## Overview

Uses the [PyQt5](https://pypi.org/project/PyQt5/) library.

Program takes in serial data through the COM port. Change the following code in `SerialHelper.py` appropriately depending on COM port, baud rate and device.

```python
    self.serArduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)     # Raspberry Pi
    self.ser = serial.Serial("COM4", 9600)                               # PC
```
Run `main.py` to run the program.

## Screenshot

![Capture](https://user-images.githubusercontent.com/39665412/79693807-6985aa80-829f-11ea-9b4b-6aa0a51bf5f4.PNG)
