# ##############################################################################
#                 INMOOV SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

inMoov=i01
if ScriptType=="Virtual":
  varduinoright = Runtime.start("varduinoright","VirtualArduino")
  varduinoright.connect(MyRightPort)
  varduinoleft = Runtime.start("varduinoleft","VirtualArduino")
  varduinoleft.connect(MyLeftPort)
#Inmoov Left / right arduino connect
if ScriptType=="RightSide" or ScriptType=="Full" or ScriptType=="Virtual":
  right = Runtime.createAndStart("i01.right", "Arduino")
  right.setBoard(BoardTypeMyRightPort)
  RightPortIsConnected=CheckArduinos(right,MyRightPort)
  
if ScriptType=="LeftSide" or ScriptType=="Full" or ScriptType=="Virtual":
  left = Runtime.createAndStart("i01.left", "Arduino")
  left.setBoard(BoardTypeMyLeftPort)
  LeftPortIsConnected=CheckArduinos(left,MyLeftPort)
  
if ScriptType=="LeftSide":talkEvent(lang_startingLeftOnly)
if ScriptType=="RightSide":talkEvent(lang_startingRightOnly)
if ScriptType=="Full":talkEvent(lang_startingFull)
if ScriptType=="NoArduino":talkEvent(lang_startingNoArduino)


