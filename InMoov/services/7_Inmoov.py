# ##############################################################################
#                 INMOOV SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

inMoov=i01
#temporary speed simulation trick ( i2c can compute speed )
if ScriptType=="Virtual":
  Platform.setVirtual(True)
  # right = Runtime.createAndStart("i01.right", "Adafruit16CServoDriver")
  # left = Runtime.createAndStart("i01.left", "Adafruit16CServoDriver")
  # virtualRaspi = Runtime.start("virtualRaspi","RasPi")
  # virtualRaspi.setWiringPi(False)
  # left.attach(virtualRaspi,"1","0x40")
  # right.attach(virtualRaspi,"1","0x41")
  right = Runtime.start("i01.right", "Arduino")
  left = Runtime.start("i01.left", "Arduino")

  RightPortIsConnected=True
  LeftPortIsConnected=True

#Inmoov Left / right arduino connect
if ScriptType=="RightSide" or ScriptType=="Full":
  right = Runtime.createAndStart("i01.right", "Arduino")
  right.setBoard(BoardTypeMyRightPort)
  RightPortIsConnected=CheckArduinos(right,MyRightPort)
  if RightPortIsConnected:right.setAref(ArefRightArduino)


if ScriptType=="LeftSide" or ScriptType=="Full":
  left = Runtime.createAndStart("i01.left", "Arduino")
  left.setBoard(BoardTypeMyLeftPort)
  LeftPortIsConnected=CheckArduinos(left,MyLeftPort)
  if LeftPortIsConnected:left.setAref(ArefLeftArduino)
  
if ScriptType=="LeftSide":i01.speakBlocking(i01.languagePack.get("startingLeftOnly"))
if ScriptType=="RightSide":i01.speakBlocking(i01.languagePack.get("startingRightOnly"))
if ScriptType=="Full":i01.speakBlocking(i01.languagePack.get("startingFull"))
if ScriptType=="NoArduino":i01.speakBlocking(i01.languagePack.get("startingNoArduino"))


