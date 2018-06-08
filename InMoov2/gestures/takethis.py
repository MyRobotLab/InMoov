
def takethis():
  fullspeed()
  inMoov.startedGesture()
  inMoov.moveHead(14,90)
  inMoov.moveArm("left",13,45,95,10)
  inMoov.moveArm("right",5,90,30,10)
  inMoov.moveHand("left",2,2,2,2,2,60)
  inMoov.moveHand("right",81,66,82,60,105,113)
  inMoov.moveTorso(85,76,90)
  sleep(3)
  inMoov.finishedGesture()
  closelefthand()
  inMoov.moveTorso(110,90,90)
  sleep(2)
  isitaball()
  inMoov.mouth.speak("what is it")
  #inMoov.mouth.speak(u"что это")

