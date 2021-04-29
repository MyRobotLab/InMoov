def slowlycloserighthand():
  i01.setArmSpeed("left",100.0,100.0,100.0,100.0)
  i01.setArmSpeed("right",100.0,36.0,100.0,100.0)
  i01.setHandSpeed("left",100.0,100.0,100.0,100.0,100.0,100.0)
  i01.setHandSpeed("right",100.0,36.0,36.0,26.0,100.0,100.0)
  i01.setHeadSpeed(36.0,36.0)
  i01.moveHead(30,60)
  i01.moveArm("right",5,80,30,10)
  i01.moveHand("right",176,173,175,175,2,180)

