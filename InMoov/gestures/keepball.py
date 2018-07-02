def keepball():
  i01.startedGesture()
  i01.setHandVelocity("left", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
  i01.setHandVelocity("right", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
  i01.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  i01.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadVelocity(50.0, 50.0)
  i01.setTorsoVelocity(31.0, 13.0, -1)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,140,140,3,0,11)
  i01.moveTorso(90,90,90)
  sleep(1)
  i01.finishedGesture()


