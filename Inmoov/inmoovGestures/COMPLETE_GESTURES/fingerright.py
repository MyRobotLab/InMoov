def fingerright():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 0.90)
  i01.setTorsoSpeed(0.9, 0.5, 1.0)
  i01.moveHead(80,86)
  i01.moveArm("left",5,94,20,10)
  i01.moveArm("right",7,78,92,10)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,2,175,160,165,180)
  i01.moveTorso(60,70,90)

