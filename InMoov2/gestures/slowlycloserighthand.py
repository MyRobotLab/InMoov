def slowlycloserighthand():
  inMoov.setArmVelocity("left",-1.0,-1.0,-1.0,-1.0)
  inMoov.setArmVelocity("right",-1,36.0,-1,-1)
  inMoov.setHandVelocity("left",-1,-1,-1,-1,-1,-1)
  inMoov.setHandVelocity("right",-1,36.0,36.0,26.0,-1,-1)
  inMoov.setHeadVelocity(36.0,36.0)
  inMoov.moveHead(30,60)
  inMoov.moveArm("right",5,80,30,10)
  inMoov.moveHand("right",176,173,175,175,2,180)

