# ##############################################################################
#                 INMOOV SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

inMoov=i01
if ScriptType=="Virtual":
  varduinoright = Runtime.start("varduinoright","VirtualArduino")
  varduinoright.serial.usedByInmoov=True
  varduinoright.connect(MyRightPort)
  varduinoleft = Runtime.start("varduinoleft","VirtualArduino")
  varduinoleft.serial.usedByInmoov=True
  varduinoleft.connect(MyLeftPort)
#Inmoov Left / right arduino connect
if ScriptType=="RightSide" or ScriptType=="Full" or ScriptType=="Virtual":
  right = Runtime.createAndStart("i01.right", "Arduino")
  right.setBoard(BoardTypeMyRightPort)
  right.usedByInmoov=True
  right.serial.usedByInmoov=True
  RightPortIsConnected=CheckArduinos(right,MyRightPort)
  if RightPortIsConnected:right.setAref(ArefRightArduino)
  
if ScriptType=="LeftSide" or ScriptType=="Full" or ScriptType=="Virtual":
  left = Runtime.createAndStart("i01.left", "Arduino")
  left.setBoard(BoardTypeMyLeftPort)
  left.usedByInmoov=True
  left.serial.usedByInmoov=True
  LeftPortIsConnected=CheckArduinos(left,MyLeftPort)
  if LeftPortIsConnected:left.setAref(ArefLeftArduino)
  
if ScriptType=="LeftSide":talkEvent(lang_startingLeftOnly)
if ScriptType=="RightSide":talkEvent(lang_startingRightOnly)
if ScriptType=="Full":talkEvent(lang_startingFull)
if ScriptType=="NoArduino":talkEvent(lang_startingNoArduino)


