def surrender():
  i01.startedGesture()
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  i01.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadVelocity(22.0, 22.0)
  i01.moveHead(90,90)
  i01.moveArm("left",90,139,15,79)
  i01.moveArm("right",90,145,37,79)
  i01.moveHand("left",50,28,30,10,10,76)
  i01.moveHand("right",10,10,10,10,10,139)
  i01.finishedGesture()

