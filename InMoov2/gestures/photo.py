def photo():
  inMoov.startedGesture()
  inMoov.moveHead(87,60)
  inMoov.moveArm("left",78,48,37,11)
  inMoov.moveArm("right",46,147,5,75)
  inMoov.moveHand("left",138,52,159,106,120,90)
  inMoov.moveHand("right",80,65,94,63,70,140)
  sleep(1)
  inMoov.finishedGesture()

