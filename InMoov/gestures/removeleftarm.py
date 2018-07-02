def removeleftarm():
  i01.startedGesture()
  i01.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  i01.setArmVelocity("left", 59, 22.0, 31.0, 31.0)
  i01.setHeadVelocity(31.0, 31.0)
  i01.moveHead(20,100)
  i01.moveArm("left",71,94,41,31)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",60,43,45,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)
  sleep(1)
  i01.finishedGesture()


