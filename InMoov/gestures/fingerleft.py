def fingerleft():
  i01.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setHandVelocity("right", -1, 43.0, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", 50, -1, -1, -1)
  i01.setHeadVelocity(-1, 50)
  i01.setTorsoVelocity(50.0, 13.0, -1)
  i01.moveHead(80,86)
  i01.moveArm("left",7,78,92,10)
  i01.moveArm("right",5,94,20,10)
  i01.moveHand("left",180,2,175,160,165,90)
  i01.moveHand("right",180,180,180,180,180,90)
  i01.moveTorso(120,110,90)


