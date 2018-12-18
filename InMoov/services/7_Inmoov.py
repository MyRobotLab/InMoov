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
  if RightPortIsConnected:right.setAref(ArefRightArduino)
  
if ScriptType=="LeftSide" or ScriptType=="Full" or ScriptType=="Virtual":
  left = Runtime.createAndStart("i01.left", "Arduino")
  left.setBoard(BoardTypeMyLeftPort)
  LeftPortIsConnected=CheckArduinos(left,MyLeftPort)
  if LeftPortIsConnected:left.setAref(ArefLeftArduino)
  
if ScriptType=="LeftSide":i01.speakBlocking(i01.languagePack.get("startingLeftOnly"))
if ScriptType=="RightSide":i01.speakBlocking(i01.languagePack.get("startingRightOnly"))
if ScriptType=="Full":i01.speakBlocking(i01.languagePack.get("startingFull"))
if ScriptType=="NoArduino":i01.speakBlocking(i01.languagePack.get("startingNoArduino"))


