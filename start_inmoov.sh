#!/bin/bash
cd "$(dirname "$0")"
echo "------------------------------------------------------"
echo "			INMOOV LAUNCHER"
echo "------------------------------------------------------"
echo "------------------------------------------------------"
echo "LOG CLEAN UP to free space disk and send clean noworky"
echo "------------------------------------------------------"
rm myrobotlab.log.1
mv myrobotlab.log myrobotlab.log.1
sleep 1
echo "."
echo "------------------------------------------------------"
echo "UPDATE MRL INSTALLATION"
echo "This may take a few minutes"
echo "------------------------------------------------------"
sleep 1
mv ./myrobotlab-*.jar ./myrobotlab.jar
if [ ./mrlNeedReinstall ]; then
	rm -r .myrobotlab
	rm -r haarcascades
	rm -r hogcascades
	rm -r lbpcascades
	rm -r libraries
	rm -r pythonModules
	rm -r resource
	rm -r tessdata
	rm ivychain.xml
	rm myrobotlab.log
	rm repo.json
	rm mrlNeedReinstall
fi
java -jar myrobotlab.jar -install
echo "Done"
echo "------------------------------------------------------"
echo "START MRL & INMOOV"
echo "------------------------------------------------------"
clear
# start the inmoov script
java -jar myrobotlab.jar -service python Python -invoke python execFile ./InMoov/InMoov.py
