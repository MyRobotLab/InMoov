def LookAtTheSky():
  inMoov.startedGesture()
  inMoov.setHeadVelocity(30,30)
  inMoov.moveHead(180,90)
  sleep(5)
  inMoov.setHeadVelocity(20, 20)
  inMoov.moveHead(90,90)
  inMoov.finishedGesture()
  