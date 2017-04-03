def slowlycloserighthand():
  i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
  i01.setArmSpeed("right",1.0,0.8,1.0,1.0)
  i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
  i01.setHandSpeed("right",1.0,0.8,0.8,0.7,1.0,1.0)
  i01.setHeadSpeed(0.8,0.8)
  i01.moveHead(30,60)
  i01.moveArm("right",5,80,30,10)
  i01.moveHand("right",176,173,175,175,2,180)

