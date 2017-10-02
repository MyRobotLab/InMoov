# -- coding: utf-8 --

def perfect():
  i01.startedGesture()
  i01.setHandSpeed("left", 0.80, 0.80, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.95, 0.95, 0.95, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
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
  

