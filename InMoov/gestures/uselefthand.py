def uselefthand():
  i01.startedGesture()
  i01.setHandVelocity("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", 6.0, 6.0, 6.0, 6.0)
  i01.setHeadVelocity(22.0, 22.0)
  i01.moveHead(10,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,61,50,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,140,145,3,0,11)
  sleep(4)
  i01.finishedGesture()

