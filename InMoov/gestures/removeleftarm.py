def removeleftarm():
  i01.startedGesture()
  i01.setHandSpeed("left", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 31.0, 43.0, 59, 43.0)
  i01.setArmSpeed("left", 59, 22.0, 31.0, 31.0)
  i01.setHeadSpeed(31.0, 31.0)
  i01.moveHead(20,100)
  i01.moveArm("left",71,94,41,31)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",60,43,45,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)
  sleep(1)
  i01.finishedGesture()


