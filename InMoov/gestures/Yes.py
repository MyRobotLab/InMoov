def Yes():
  if isHeadActivated==1:
    inMoov.startedGesture()
    inMoov.setHeadVelocity(45,45,45)
    inMoov.moveHeadBlocking(130,90)
    inMoov.moveHeadBlocking(50,93)
    inMoov.moveHeadBlocking(120,88)
    inMoov.moveHeadBlocking(70,90)
    inMoov.moveHeadBlocking(90,90)
    inMoov.finishedGesture()