# ##############################################################################
# 								ARDUINO SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if ScriptType=="RightSide" or ScriptType=="Full":
	right = Runtime.createAndStart("i01.right", "Arduino")
if ScriptType=="LeftSide" or ScriptType=="Full":
	left = Runtime.createAndStart("i01.left", "Arduino")

# ##############################################################################
# ARDUINO RELATED FUNCTIONS
# ##############################################################################


def CheckArduinos(Card,Port):
	
	Card.connect(Port)
	if not Card.isConnected():
		errorSpokenFunc('ArduinoNotConnected',Port)
	return Card.isConnected()
	