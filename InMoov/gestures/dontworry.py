# -- coding: utf-8 --
def dontworry():
  i01.startedGesture()
  i01.setHandVelocity("left", 50, 50, 50, 50, 50, 59)
  i01.setHandVelocity("right", 50, 50, 50, 50, 50, 59)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", 50, -1, -1, -1)
  i01.moveHead(116,80)
  i01.moveArm("left",85,93,42,16)
  i01.moveArm("right",87,93,37,18)
  i01.moveHand("left",124,82,65,81,41,143)
  i01.moveHand("right",59,53,89,61,36,21)
  i01.moveTorso(90,90,90)
  i01.mouth.speak("mmmmmmh, I sense much fear in you")
  #i01.mouth.speak(u"Ммммммх, я чувствую большой страх в тебе")
  sleep(2)
  i01.finishedGesture()
  relax()
    
