def tiltHeadAgree():
  i01.startedGesture()
  i01.setHeadVelocity(60, 60, 70)
  i01.moveHead(80,90,180)
  sleep(0.8)
  i01.moveHead(90,90,90)
  i01.finishedGesture()
