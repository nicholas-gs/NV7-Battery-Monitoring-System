# NV7 Battery Monitoring System

## __SerialHelper__

### Class ComPort(QThread)

Assumptions about incoming data stream from the COM Port

1. Incoming data stream has length 5 or 6
    1. 1st char is the module index
    2. 2nd & 3rd char is the thermistor id
    3. 4th & 5th is the temperature
    4. Ignore the 6th char if present

A background thread continously reads in the COM Port data. When the module index changes between read in, the data is passed to the main thread for display