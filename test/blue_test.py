from smd.blue import *
from smd.red import *

port = SerialPort("COM9", baudrate=2000000, timeout=0.01)
red_1 = Red(0, port)
blue = Blue(0, port)
#print(scan_blue_devices(port))

#blue.set_variables([Index_Blue.OperationMode, Blue.Operation_Mode.Position_Internal_Trajectory])
#blue.enter_operation()
blue.enable_torque(True)

#blue.set_variables([Index_Blue.Microstepping, 2])

#blue.enter_configuration()
#blue.set_variables([Index_Blue.TargetPosition, 100000])


#blue.set_variables([Index_Blue.Config_TimeStamp, 123])
#blue.set_variables([Index_Blue.Config_Description, ''])

#blue.set_config_description()
#blue.set_config_timeStamp()

