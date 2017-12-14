def Yes():
  if isHeadActivated==1:
    i01.startedGesture()
    i01.setHeadVelocity(45,45,45)
    i01.moveHeadBlocking(130,90)
    i01.moveHeadBlocking(50,93)
    i01.moveHeadBlocking(120,88)
    i01.moveHeadBlocking(70,90)
    i01.moveHeadBlocking(90,90)
    i01.finishedGesture()