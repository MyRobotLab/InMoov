# -- coding: utf-8 --

def rollHead():
  i01.startedGesture()
  i01.setHeadVelocity(70, 70, 70)
  i01.moveHead(90,90,20)
  sleep(0.5)
  i01.moveHead(90,90,170)
  sleep(1)
  i01.moveHead(90,90,20)
  sleep(1)
  i01.moveHead(90,90,170)
  sleep(1)
  i01.moveHead(90,90,90)
  sleep(1)
  i01.mouth.speakBlocking("thanks a lot, it feels great. doctor")
  #i01.mouth.speakBlocking(u"Большое спасибо, он чувствует себя прекрасно. Доктор")
  i01.finishedGesture()
