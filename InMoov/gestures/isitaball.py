def isitaball():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", -1, -1, -1, 36.0, 36.0, 50)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("right", -1, 59, 59, 43.0)
  inMoov.setArmVelocity("left", 31.0, 43.0, 50, 43.0)
  inMoov.setHeadVelocity(22.0, 31.0)
  inMoov.moveHead(70,82)
  fullspeed()
  inMoov.moveArm("left",70,59,95,15)
  inMoov.moveArm("right",12,74,33,15)
  inMoov.moveHand("left",170,150,180,180,180,164)
  inMoov.moveHand("right",105,81,78,57,62,105)
  sleep(1)
  inMoov.finishedGesture()
  

