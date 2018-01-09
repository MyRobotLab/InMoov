def more():
  i01.startedGesture()
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.80, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(13,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",80,114,114,3,0,11)
  sleep(3)
  i01.finishedGesture()

