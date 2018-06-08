
def dontworry():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", 50, 50, 50, 50, 50, 59)
  inMoov.setHandVelocity("right", 50, 50, 50, 50, 50, 59)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("right", 50, -1, -1, -1)
  inMoov.moveHead(116,80)
  inMoov.moveArm("left",85,93,42,16)
  inMoov.moveArm("right",87,93,37,18)
  inMoov.moveHand("left",124,82,65,81,41,143)
  inMoov.moveHand("right",59,53,89,61,36,21)
  inMoov.moveTorso(90,90,90)
  inMoov.mouth.speak("mmmmmmh, I sense much fear in you")
  #inMoov.mouth.speak(u"Ммммммх, я чувствую большой страх в тебе")
  sleep(2)
  inMoov.finishedGesture()
  relax()
    
