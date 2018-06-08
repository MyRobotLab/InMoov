def surrender():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  inMoov.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
  inMoov.setHeadVelocity(22.0, 22.0)
  inMoov.moveHead(90,90)
  inMoov.moveArm("left",90,139,15,79)
  inMoov.moveArm("right",90,145,37,79)
  inMoov.moveHand("left",50,28,30,10,10,76)
  inMoov.moveHand("right",10,10,10,10,10,139)
  inMoov.finishedGesture()

