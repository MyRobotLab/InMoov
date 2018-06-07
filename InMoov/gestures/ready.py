
def ready():
  inMoov.mouth.speak("ready")
  #inMoov.mouth.speak(u"готов")
  inMoov.mouth.speak("go")
  #inMoov.mouth.speak(u"Вперёд")
  inMoov.moveHead(90,90)
  inMoov.moveArm("left",65,90,75,10)
  inMoov.moveArm("right",20,80,25,20)
  inMoov.moveHand("left",130,180,180,180,180,90)
  inMoov.moveHand("right",50,90,90,90,100,90)



