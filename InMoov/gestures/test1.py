def test1():
  rest()
  i01.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(50.0, 50.0)
  i01.setTorsoVelocity(-1, -1, -1)
  i01.moveHead(50,110)
  i01.moveArm("left",88,90,70,23)
  i01.moveArm("right",73,90,70,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)
  sleep(2)


