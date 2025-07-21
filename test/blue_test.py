from smd.blue import *
from smd.red import *

port = SerialPort("COM9", baudrate=2000000, timeout=0.01)
red_1 = Red(0, port)
blue = Blue(0, port)
#print(scan_blue_devices(port))

def configure():
    blue.set_variables([Index_Blue.OperationMode, Blue.Operation_Mode.Position_Internal_Trajectory])
    blue.set_microstepping(Blue.microStepping.FULL_STEP, False, Blue.autoStepInterpolation._256_Interpolation)





#blue.set_config_timeStamp()
text = "hello " + 90*"a" + "end" + " " + "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
text2 = "hello world"
#blue.set_config_description(text)
blue.set_config_description(text)

#configure()
#blue.enter_operation()
#blue.enable_torque(True)
#blue.set_variables([Index_Blue.TargetPosition, 6000])


#blue.enter_configuration()



#blue.set_variables([Index_Blue.Config_TimeStamp, 123])
#blue.set_variables([Index_Blue.Config_Description, ''])

#blue.set_config_description()
#blue.set_config_timeStamp()




