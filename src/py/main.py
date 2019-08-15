
import win32com.client as RobotOM
import os
import sys

"""
import clr
from System import Object


dll_path = rob_dir + "\\Interop.RobotOM.dll"

clr.AddReference(dll_path)
print dll_path
from RobotOM import *

rob = RobotApplicationClass()
# _str = rob.Project.Structure
"""

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

