def tiltHeadAgree():
  inMoov.startedGesture()
  inMoov.setHeadVelocity(60, 60, 70)
  inMoov.moveHead(80,90,180)
  sleep(0.8)
  inMoov.moveHead(90,90,90)
  inMoov.finishedGesture()
