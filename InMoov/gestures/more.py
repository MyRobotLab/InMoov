def more():
  inMoov.startedGesture()
  inMoov.setHandVelocity("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  inMoov.setArmVelocity("left", 43.0, 36, 43.0, 59)
  inMoov.setArmVelocity("right", 31.0, 22.0, 22.0, 22.0)
  inMoov.setHeadVelocity(22.0, 22.0)
  inMoov.moveHead(13,80)
  inMoov.moveArm("left",64,52,59,23)
  inMoov.moveArm("right",75,60,50,16)
  inMoov.moveHand("left",140,148,140,10,10,0)
  inMoov.moveHand("right",80,114,114,3,0,11)
  sleep(3)
  inMoov.finishedGesture()

