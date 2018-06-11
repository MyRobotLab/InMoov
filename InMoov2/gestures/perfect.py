
def perfect():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", 36, 36, -1, -1, -1, -1)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("left", 59, 59, 59, -1)
  inMoov.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  inMoov.setHeadVelocity(22.0, 31.0)
  inMoov.moveHead(88,79)
  inMoov.moveArm("left",89,75,93,11)
  inMoov.moveArm("right",0,91,28,17)
  inMoov.moveHand("left",130,160,83,40,0,34)
  inMoov.moveHand("right",86,51,133,162,153,180)
  sleep(1)
  inMoov.mouth.speak("it is perfect")
  sleep(1)
  inMoov.finishedGesture()
  #inMoov.mouth.speak(u"Это идеально")
  

