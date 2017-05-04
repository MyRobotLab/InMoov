def daVinci():
  rightArm.enableAutoDisable(0)
  leftArm.enableAutoDisable(0)
  inMoov.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
  inMoov.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
  inMoov.setArmSpeed("left", 0.80, 0.80, 0.80, 0.80)
  inMoov.setArmSpeed("right", 0.80, 0.80, 0.80, 0.80)
  inMoov.setHeadSpeed(0.75, 0.75)
  inMoov.moveHead(80,90)
  inMoov.moveArm("left",0,118,29,74)
  inMoov.moveArm("right",0,118,29,74)
  inMoov.moveHand("left",50,40,30,20,10,47)
  inMoov.moveHand("right",50,40,30,20,10,137)

