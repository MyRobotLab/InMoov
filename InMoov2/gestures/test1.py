def test1():
  rest()
  inMoov.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  inMoov.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  inMoov.setHeadVelocity(50.0, 50.0)
  inMoov.setTorsoVelocity(-1, -1, -1)
  inMoov.moveHead(50,110)
  inMoov.moveArm("left",88,90,70,23)
  inMoov.moveArm("right",73,90,70,27)
  inMoov.moveHand("left",2,2,2,2,2,90)
  inMoov.moveHand("right",2,2,2,2,2,90)
  inMoov.moveTorso(90,90,90)
  sleep(2)


