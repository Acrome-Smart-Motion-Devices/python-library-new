from smd.blue import *
from smd.red import *
from smd.green import *

port = SerialPort("COM14", baudrate=921600, timeout=0.1, isTest=False)
dev = Green(0, port)





while True:
    #input()
    print(dev.get_FOC_parameters(0))
    #time.sleep(0.01)






#blue.set_variables([Index_Blue.Config_TimeStamp, 123])
#blue.set_variables([Index_Blue.Config_Description, ''])

#blue.set_config_description()
#blue.set_config_timeStamp()




