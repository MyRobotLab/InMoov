def giving():
  inMoov.startedGesture()
  fullspeed()
  if (inMoov.RobotIsOpenCvCapturing()):
    #inMoov.moveHead(44,82)
    inMoov.moveArm("left",15,55,68,10)
    inMoov.moveArm("right",13,40,74,13)
    inMoov.moveHand("left",61,0,14,0,0,180)
    inMoov.moveHand("right",0,24,24,19,21,25)
    inMoov.moveTorso(90,90,90)

  else:
    inMoov.moveHead(44,82)
    inMoov.moveArm("left",15,55,68,10)
    inMoov.moveArm("right",13,40,74,13)
    inMoov.moveHand("left",61,0,14,0,0,180)
    inMoov.moveHand("right",0,24,24,19,21,25)
    inMoov.moveTorso(90,90,90)
  inMoov.finishedGesture() 
