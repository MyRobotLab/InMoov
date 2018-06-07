def uselefthand():
  inMoov.startedGesture()
  inMoov.setHandVelocity("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("right", 6.0, 6.0, 6.0, 6.0)
  inMoov.setHeadVelocity(22.0, 22.0)
  inMoov.moveHead(10,80)
  inMoov.moveArm("left",64,52,59,23)
  inMoov.moveArm("right",75,61,50,16)
  inMoov.moveHand("left",130,0,40,10,10,0)
  inMoov.moveHand("right",180,140,145,3,0,11)
  sleep(4)
  inMoov.finishedGesture()

