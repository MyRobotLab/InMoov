def handdown():
  i01.startedGesture()
  i01.setHandVelocity("left", 31.0, 31.0, 31.0, 31.0, 31.0, 31.0)
  i01.setHandVelocity("right", 26.00, 26.00, 26.00, 26.00, 26.00, -1)
  i01.setArmVelocity("right", 43.0, 22.0, 22.0, 22.0)
  i01.moveHead(18,75)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",54,95,66,0,0,11)
  sleep(2)
  i01.finishedGesture()

