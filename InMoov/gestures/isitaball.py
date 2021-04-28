def isitaball():
  i01.startedGesture()
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 36.0, 36.0, 50)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 59, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 50, 43.0)
  i01.setHeadSpeed(22.0, 31.0)
  i01.moveHead(70,82)
  fullspeed()
  i01.moveArm("left",70,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)
  sleep(1)
  i01.finishedGesture()
  

