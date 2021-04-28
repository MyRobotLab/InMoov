def test1():
  rest()
  i01.setHandSpeed("left", 43.0, 43.0, 43.0, 43.0, 43.0, 100.0)
  i01.setHandSpeed("right", 43.0, 43.0, 43.0, 43.0, 43.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(50.0, 50.0)
  i01.setTorsoSpeed(100.0, 100.0, 100.0)
  i01.moveHead(50,110)
  i01.moveArm("left",88,90,70,23)
  i01.moveArm("right",73,90,70,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)
  sleep(2)


