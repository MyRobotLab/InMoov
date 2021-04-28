def perfect():
  i01.startedGesture()
  i01.setHandSpeed("left", 36, 36, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 59, 59, 59, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(22.0, 31.0)
  i01.moveHead(88,79)
  i01.moveArm("left",89,75,93,11)
  i01.moveArm("right",0,91,28,17)
  i01.moveHand("left",130,160,83,40,0,34)
  i01.moveHand("right",86,51,133,162,153,180)
  sleep(1)
  i01.mouth.speak("it is perfect")
  sleep(1)
  i01.finishedGesture()
  #i01.mouth.speak(u"Это идеально")
  

