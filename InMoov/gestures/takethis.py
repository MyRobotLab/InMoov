# -- coding: utf-8 --

def takethis():
  fullspeed()
  i01.startedGesture()
  i01.moveHead(14,90)
  i01.moveArm("left",13,45,95,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",2,2,2,2,2,60)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(85,76,90)
  sleep(3)
  i01.finishedGesture()
  closelefthand()
  i01.moveTorso(110,90,90)
  sleep(2)
  isitaball()
  i01.mouth.speak("what is it")
  #i01.mouth.speak(u"что это")

