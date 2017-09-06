# -- coding: utf-8 --

def speakhindi():
  i01.mouth.speak("yes, i can speak any language")
  #i01.mouth.speak(u"Да, я могу говорить на любом языке")
  i01.moveHead(116,80)
  i01.moveArm("left",85,93,42,16)
  i01.moveArm("right",87,93,37,18)
  i01.moveHand("left",124,82,65,81,41,143)
  i01.moveHand("right",59,53,89,61,36,21)
  i01.moveTorso(90,90,90)
  sleep(0.2)
  sleep(1)
  relax()
