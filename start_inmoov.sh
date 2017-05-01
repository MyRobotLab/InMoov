#!/bin/bash



echo "------------------------------------------------------"
echo "			INMOOV LAUNCHER"
echo "------------------------------------------------------"

echo "------------------------------------------------------"
echo "LOG CLEAN UP to free space disk and send clean noworky"
echo "------------------------------------------------------"

rm myrobotlab.log.1
mv myrobotlab.log myrobotlab.log.1

echo "."
echo "------------------------------------------------------"
echo "UPDATE MRL INSTALLATION"
echo "This may take a few minutes"
echo "------------------------------------------------------"

java -jar myrobotlab.jar -install

echo "Done"
echo "------------------------------------------------------"
echo "START MRL & INMOOV"
echo "------------------------------------------------------"

clear
# start the inmoov script
java -jar myrobotlab.jar -invoke python execFile ./InMoov/InMoov.py -service python Python

