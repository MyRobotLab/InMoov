def giving():
  i01.startedGesture()
  fullspeed()
  if (i01.RobotIsOpenCvCapturing()):
    #i01.moveHead(44,82)
    i01.moveArm("left",15,55,68,10)
    i01.moveArm("right",13,40,74,13)
    i01.moveHand("left",61,0,14,0,0,180)
    i01.moveHand("right",0,24,24,19,21,25)
    i01.moveTorso(90,90,90)

  else:
    i01.moveHead(44,82)
    i01.moveArm("left",15,55,68,10)
    i01.moveArm("right",13,40,74,13)
    i01.moveHand("left",61,0,14,0,0,180)
    i01.moveHand("right",0,24,24,19,21,25)
    i01.moveTorso(90,90,90)
  i01.finishedGesture() 
