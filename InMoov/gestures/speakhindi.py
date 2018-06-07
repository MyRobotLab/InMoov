
def speakhindi():
  inMoov.mouth.speak("yes, i can speak any language")
  #inMoov.mouth.speak(u"Да, я могу говорить на любом языке")
  inMoov.moveHead(116,80)
  inMoov.moveArm("left",85,93,42,16)
  inMoov.moveArm("right",87,93,37,18)
  inMoov.moveHand("left",124,82,65,81,41,143)
  inMoov.moveHand("right",59,53,89,61,36,21)
  inMoov.moveTorso(90,90,90)
  sleep(0.2)
  sleep(1)
  relax()
