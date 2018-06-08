def dropit():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  inMoov.setArmVelocity("left", 31.0, 43.0, -1, 43.0)
  inMoov.setHeadVelocity(31.0, 31.0)
  inMoov.moveHead(20,99)
  inMoov.moveArm("left",5,45,87,31)
  inMoov.moveArm("right",5,82,33,15)
  sleep(3)
  inMoov.moveHand("left",60,61,67,34,34,35)
  inMoov.moveHand("right",20,40,40,30,30,72)
  sleep(2)
  inMoov.finishedGesture()





