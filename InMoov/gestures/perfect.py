def perfect():
  i01.startedGesture()
  i01.setHandVelocity("left", 36, 36, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", 59, 59, 59, -1)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(22.0, 31.0)
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
  

