import pytermgui as ptg
import time

import HardwareMonitor.Hardware as Hardware

class UpdateVisitor:
    def VisitComputer(computer):
        user.Traverse(self)

    def VisitHardware(hardware):
        Hardware.Hardware.Update()
        for subHardware in Hardware.Hardware.SubHardware:
            subHardware.Accept()

    def VisitSensor(sensor):
        None
    def VisitParameter(parameter):
        None

user = Hardware.Computer()
user.IsMotherboardEnabled = True
user.IsControllerEnabled = True
user.IsCpuEnabled = True
user.IsGpuEnabled = True
user.IsBatteryEnabled = True
user.IsMemoryEnabled = True
user.IsNetworkEnabled = True
user.IsStorageEnabled = True
user.Open()

for hardware in user.Hardware:
    print("Hardware: ", hardware.Name, " Type: ", hardware.HardwareType)

# def macro_temp(x: str) -> str:
    

# ptg.tim.define("!temp", macro_temp)

# with ptg.WindowManager() as manager:
#     manager.layout.add_slot("Body")
#     manager.add(
#         ptg.Window("[!temp]CPU", box="EMPTY")
#     )
#asdasdasda
# with ptg.WindowManager() as manager:
#     for 

#     window = ptg.Window(
        
#     )

#     layout = manager.layout
#     layout.add_slot("body")

#     manager.add(window, assign="body")