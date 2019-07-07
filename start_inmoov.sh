#!/bin/bash

#############################################################
# InMoov Unix Start Script 
# Usage:  ./start_inmoov.sh
# This will launch MyRobotLab and run the InMoov.py 
# default startup script
#############################################################

echo "------------------------------------------------------"
echo "			INMOOV LAUNCHER"
echo "------------------------------------------------------"
echo "Rotate Log files for clean no worky logs"
echo "------------------------------------------------------"
rm myrobotlab.log.1
mv myrobotlab.log myrobotlab.log.1
echo "Done."
echo "------------------------------------------------------"
echo "START MRL & INMOOV"
echo "------------------------------------------------------"
# start the inmoov script
java -jar myrobotlab.jar --service python Python --invoke python execFile ./InMoov/InMoov.py