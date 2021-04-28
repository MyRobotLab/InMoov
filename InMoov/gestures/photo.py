def photo():
  i01.startedGesture()
  i01.moveHead(87,60)
  i01.moveArm("left",78,48,37,11)
  i01.moveArm("right",46,147,5,75)
  i01.moveHand("left",138,52,159,106,120,90)
  i01.moveHand("right",80,65,94,63,70,140)
  sleep(1)
  i01.finishedGesture()

