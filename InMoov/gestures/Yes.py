def Yes():
  if isHeadActivated==1:
    i01.startedGesture()
    i01.setHeadVelocity(80,80,80)
    i01.moveHead(50,93)
    sleep(0.3)
    i01.moveHead(120,88)
    sleep(0.3)
    i01.moveHead(70,90)
    sleep(0.4)
    i01.moveHead(90,90)
    i01.finishedGesture()
