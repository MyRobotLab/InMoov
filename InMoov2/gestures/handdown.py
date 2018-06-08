def handdown():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", 31.0, 31.0, 31.0, 31.0, 31.0, 31.0)
  inMoov.setHandVelocity("right", 26.00, 26.00, 26.00, 26.00, 26.00, -1)
  inMoov.setArmVelocity("right", 43.0, 22.0, 22.0, 22.0)
  inMoov.moveHead(18,75)
  inMoov.moveArm("left",66,52,59,23)
  inMoov.moveArm("right",59,60,50,16)
  inMoov.moveHand("left",140,148,140,10,10,0)
  inMoov.moveHand("right",54,95,66,0,0,11)
  sleep(2)
  inMoov.finishedGesture()

