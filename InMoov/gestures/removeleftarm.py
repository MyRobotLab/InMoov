def removeleftarm():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  inMoov.setArmVelocity("left", 59, 22.0, 31.0, 31.0)
  inMoov.setHeadVelocity(31.0, 31.0)
  inMoov.moveHead(20,100)
  inMoov.moveArm("left",71,94,41,31)
  inMoov.moveArm("right",5,82,28,15)
  inMoov.moveHand("left",60,43,45,34,34,35)
  inMoov.moveHand("right",20,40,40,30,30,72)
  sleep(1)
  inMoov.finishedGesture()


