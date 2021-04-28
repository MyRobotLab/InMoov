def keepball():
  i01.startedGesture()
  i01.setHandSpeed("left", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setArmSpeed("right", 31.0, 43.0, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadSpeed(50.0, 50.0)
  i01.setTorsoSpeed(31.0, 13.0, 100.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,140,140,3,0,11)
  i01.moveTorso(90,90,90)
  sleep(1)
  i01.finishedGesture()


