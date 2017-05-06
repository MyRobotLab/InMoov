def daVinci():
  i01.rightArm.enableAutoDisable(0)
  i01.leftArm.enableAutoDisable(0)
  i01.inMoov.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
  i01.inMoov.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
  i01.inMoov.setArmSpeed("left", 0.80, 0.80, 0.80, 0.80)
  i01.inMoov.setArmSpeed("right", 0.80, 0.80, 0.80, 0.80)
  i01.inMoov.setHeadSpeed(0.75, 0.75)
  i01.inMoov.moveHead(80,90)
  i01.inMoov.moveArm("left",0,118,29,74)
  i01.inMoov.moveArm("right",0,118,29,74)
  i01.inMoov.moveHand("left",50,40,30,20,10,47)
  i01.inMoov.moveHand("right",50,40,30,20,10,137)

