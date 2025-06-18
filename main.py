import pytermgui as ptg
from pytermgui import Layout
from time import sleep

import HardwareMonitor.Hardware as Hardware
from HardwareMonitor.Util import *

user = OpenComputer(motherboard=True, controller=True, cpu=True, gpu=True, battery=True, memory=True, network=True, storage=True)

CPU: str = None
GPU: str = None

def setHwVariables() -> None:
    global CPU
    global GPU
    for hw in user.Hardware:
        if str(hw.HardwareType) == ("Cpu"):
            CPU = str(hw.HardwareType)
        if str(hw.HardwareType).find("Gpu") >= 0:
            GPU = str(hw.HardwareType)
setHwVariables()

ticker = 0
def macro_ticker(a: None) -> str:
    global ticker
    if ticker <= 20:
        ticker += 1
    elif ticker > 20:
        ticker = 0
        user.Update()
    return " "


def macro_getCPUTemp(a: None) -> str:
    sensors = next((x.Sensors for x in user.Hardware if str(x.HardwareType) == CPU), None)
    temps: list = []
    for x in sensors:
        if str(x.SensorType) == "Temperature":
            sensorName = str(x.Name)
            if sensorName.find("Core #") >= 0 and sensorName.find("to") == -1:
                temps.append(x.Value)
    return str(sum(temps) / len(temps))

def macro_getGPUTemp(a: None) -> str:
    sensors = next((x.Sensors for x in user.Hardware if str(x.HardwareType) == GPU), None)
    temps: list = []
    for x in sensors:
        if str(x.SensorType) == "Temperature":
            sensorName = str(x.Name)
            if sensorName.find("Core") >= 0:
                temps.append(x.Value)
    return str(sum(temps) / len(temps))

ptg.tim.define("!cputemp", macro_getCPUTemp)
ptg.tim.define("!gputemp", macro_getGPUTemp)
ptg.tim.define("!ticker", macro_ticker)

with ptg.WindowManager() as manager:
    manager.layout = Layout()
    lo = manager.layout
    lo.add_slot("header", height=4)
    lo.add_slot("rightheader", width=0.3)
    lo.add_break()
    lo.add_slot("body1", width=0.25)
    lo.add_slot("body2", width=0.25)
    lo.add_slot("body3", width=0.25)
    lo.add_slot("body4", width=0.25)
    lo.add_break()
    lo.add_slot("footer", height=4)
    lo.add_slot("rightfooter", width=0.3)
    lo.add_break()
    lo.add_slot("footerfooter", height=1)

    manager.add(
        ptg.Window(
            "[bold italic orangered]Stove[/][dim]\nv0.0.0.0",
            is_static=True
        ), assign="header"
    )
    manager.add(
        ptg.Window(
            "",
            is_static=True
        ), assign="rightheader"
    )
    manager.add(
        ptg.Window(
            "CPU Temp\n\n[bold orange !cputemp]#[/]C",
            is_static=True
        ), assign="body1"
    )
    manager.add(
        ptg.Window(
            "GPU Temp\n\n[bold orange !gputemp]#[/]C",
            is_static=True
        ), assign="body2"
    )
    manager.add(
        ptg.Window(
            "[!ticker]#[/]",
            box="EMPTY",
            is_static=True
        ), assign="footerfooter"
    )