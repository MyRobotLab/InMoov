def dropit():
  i01.startedGesture()
  i01.setHandSpeed("left", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 31.0, 43.0, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 100.0, 43.0)
  i01.setHeadSpeed(31.0, 31.0)
  i01.moveHead(20,99)
  i01.moveArm("left",5,45,87,31)
  i01.moveArm("right",5,82,33,15)
  sleep(3)
  i01.moveHand("left",60,61,67,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)
  sleep(2)
  i01.finishedGesture()





