def keepball():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
  inMoov.setHandVelocity("right", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
  inMoov.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  inMoov.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
  inMoov.setHeadVelocity(50.0, 50.0)
  inMoov.setTorsoVelocity(31.0, 13.0, -1)
  inMoov.moveHead(20,70)
  inMoov.moveArm("left",5,84,16,15)
  inMoov.moveArm("right",54,77,55,16)
  inMoov.moveHand("left",50,50,40,20,20,90)
  inMoov.moveHand("right",180,140,140,3,0,11)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  inMoov.finishedGesture()


