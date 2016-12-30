# ##############################################################################
# 								INMOOV SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

#Inmoov Left / right
if ScriptType=="RightSide" or ScriptType=="Full":
	right = Runtime.createAndStart("i01.right", "Arduino")
	RightPortIsConnected=CheckArduinos(right,MyRightPort)
	
if ScriptType=="LeftSide" or ScriptType=="Full":
	left = Runtime.createAndStart("i01.left", "Arduino")
	LeftPortIsConnected=CheckArduinos(left,MyLeftPort)
