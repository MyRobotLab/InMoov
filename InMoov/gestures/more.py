def more():
  i01.startedGesture()
  i01.setHandSpeed("right", 31.0, 31.0, 31.0, 31.0, 31.0, 22.0)
  i01.setArmSpeed("left", 43.0, 36, 43.0, 59)
  i01.setArmSpeed("right", 31.0, 22.0, 22.0, 22.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.moveHead(13,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",80,114,114,3,0,11)
  sleep(3)
  i01.finishedGesture()

