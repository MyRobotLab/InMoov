def victory():
  inMoov.startedGesture()
  inMoov.moveHead(114,90)
  inMoov.moveArm("left",90,91,106,10)
  inMoov.moveArm("right",0,73,30,17)
  inMoov.moveHand("left",170,0,0,168,167,0)
  inMoov.moveHand("right",98,37,34,67,118,166)
  inMoov.moveTorso(90,90,90)
  inMoov.finishedGesture()
