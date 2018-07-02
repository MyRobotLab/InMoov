def slowlycloserighthand():
  i01.setArmVelocity("left",-1.0,-1.0,-1.0,-1.0)
  i01.setArmVelocity("right",-1,36.0,-1,-1)
  i01.setHandVelocity("left",-1,-1,-1,-1,-1,-1)
  i01.setHandVelocity("right",-1,36.0,36.0,26.0,-1,-1)
  i01.setHeadVelocity(36.0,36.0)
  i01.moveHead(30,60)
  i01.moveArm("right",5,80,30,10)
  i01.moveHand("right",176,173,175,175,2,180)

