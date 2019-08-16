
# Entry point for the api call

import win32com.client as RobotOM
import os

rob_dir = "C:\\Program Files\\Autodesk\\Autodesk Robot Structural Analysis Professional 2017\\System\\Exe"
rob_exe = rob_dir + "\\robot.exe"


def apiCall(call="link"):
    if call == "link":
        print "Robot called to link. Please wait..."
        robapp = RobotOM.Dispatch("Robot.Application")

    elif call == "start":
        print "Robot called to start."
        robapp = os.startfile(rob_exe)
    return robapp
