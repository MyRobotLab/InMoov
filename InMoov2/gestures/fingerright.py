def fingerright():
  inMoov.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  inMoov.setHandVelocity("right", -1, 43.0, -1, -1, -1, -1)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("right", 50, -1, -1, -1)
  inMoov.setHeadVelocity(-1, 50)
  inMoov.setTorsoVelocity(50.0, 13.0, -1)
  inMoov.moveHead(80,86)
  inMoov.moveArm("left",5,94,20,10)
  inMoov.moveArm("right",7,78,92,10)
  inMoov.moveHand("left",180,180,180,180,180,90)
  inMoov.moveHand("right",180,2,175,160,165,180)
  inMoov.moveTorso(60,70,90)

