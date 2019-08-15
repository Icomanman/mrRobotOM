
import os
import sys

dirname = os.getcwd()
sys.path.append(dirname + "\\src\\py")
sys.path.append(dirname + "\\ref")

import main
import barData

rob = main.apiCall("link")

if rob.Visible:
    print "succesfully connected."
else:
    print "No instance of Robot found. Exiting..."
    sys.exit()

bars = barData.selectedBeams(rob)
barData.getNodes(rob.bars)
