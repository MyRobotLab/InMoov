# ##############################################################################
# 								INMOOV SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

inMoov=i01
#varduinoright = Runtime.start("varduinoright","VirtualArduino")
#varduinoright.connect(MyRightPort)
#varduinoleft = Runtime.start("varduinoleft","VirtualArduino")
#varduinoleft.connect(MyLeftPort)
#Inmoov Left / right arduino connect
if ScriptType=="RightSide" or ScriptType=="Full":
	right = Runtime.createAndStart("i01.right", "Arduino")
	RightPortIsConnected=CheckArduinos(right,MyRightPort)
	
if ScriptType=="LeftSide" or ScriptType=="Full":
	left = Runtime.createAndStart("i01.left", "Arduino")
	LeftPortIsConnected=CheckArduinos(left,MyLeftPort)
	
if ScriptType=="LeftSide":talkEvent(lang_startingLeftOnly)
if ScriptType=="RightSide":talkEvent(lang_startingRightOnly)
if ScriptType=="Full":talkEvent(lang_startingFull)
if ScriptType=="NoArduino":talkEvent(lang_startingNoArduino)