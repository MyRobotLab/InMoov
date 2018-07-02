def dropit():
  i01.startedGesture()
  i01.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  i01.setArmVelocity("left", 31.0, 43.0, -1, 43.0)
  i01.setHeadVelocity(31.0, 31.0)
  i01.moveHead(20,99)
  i01.moveArm("left",5,45,87,31)
  i01.moveArm("right",5,82,33,15)
  sleep(3)
  i01.moveHand("left",60,61,67,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)
  sleep(2)
  i01.finishedGesture()





