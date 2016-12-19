# ##############################################################################
# 								ARDUINO SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

right = Runtime.createAndStart("i01.right", "Arduino")

# ##############################################################################
# ARDUINO RELATED FUNCTIONS
# ##############################################################################


RightPortIsConnected=0
def CheckArduinos():
	if ScriptType=="FingerStarter":
		RightPortIsConnected=right.connect(MyRightPort)
		RightPortIsConnected=right.isConnected()
		if not RightPortIsConnected:
			errorSpokenFunc('RightPortIsConnected')