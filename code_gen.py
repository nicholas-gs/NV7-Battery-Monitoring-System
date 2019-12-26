i = 0
while(i < 32):
    print(""" if(tempData[""" + str(i) + """] != 0):
    self.mod5_""" + str(i) + """.display(tempData[""" + str(i) + """])
    palette = self.mod5_""" + str(i) + """.palette()      
    palette.setColor(palette.Background, Ui_MainWindow.greenColor)
    self.mod5_""" + str(i) + """.setPalette(palette)
else:
    palette = self.mod5_""" + str(i) + """.palette()      
    palette.setColor(palette.Background, Ui_MainWindow.yellowColor)
    self.mod5_""" + str(i) + """.setPalette(palette)
    """)

    i += 1
