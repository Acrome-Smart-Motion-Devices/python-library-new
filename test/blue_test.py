from smd.blue import *
from smd.red import *


port = SerialPort("COM9", baudrate=2000000, timeout=0.1)

blue = Blue(0,port)
red = Red(15,port)



print(blue.get_variables(Index_Blue.MaxAcceleration))


#print(scan_Red_Devices(port))
#print(scan_BLUE_devices(port))