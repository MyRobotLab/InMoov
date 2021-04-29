def fingerleft():
  i01.setHandSpeed("left", 43.0, 43.0, 43.0, 43.0, 43.0, 100.0)
  i01.setHandSpeed("right", 100.0, 43.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 50, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(100.0, 50)
  i01.setTorsoSpeed(50.0, 13.0, 100.0)
  i01.moveHead(80,86)
  i01.moveArm("left",7,78,92,10)
  i01.moveArm("right",5,94,20,10)
  i01.moveHand("left",180,2,175,160,165,90)
  i01.moveHand("right",180,180,180,180,180,90)
  i01.moveTorso(120,110,90)


