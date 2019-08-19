# starting point of the script
import os
import sys

dirname = os.getcwd()
sys.path.append(dirname + "\\src\\py")
sys.path.append(dirname + "\\src\\py\\helpers")

import main
import init
import results

rob = main.apiCall("link")

if rob.Visible:
    print "App succesfully connected."
else:
    print "No instance of Robot found. Exiting..."
    # ADD user prompt to open robot?
    sys.exit()

# init.run(rob)

results.pullResults(rob)
