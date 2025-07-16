from smd.blue import *
from smd.red import *


port = SerialPort("COM9", isTest=True)

blue = Blue(0,port,True)
red = Red(0,port,True)


blue.ping()
red.ping()



scan_SMD_Red_Devices(port)