# -- coding: utf-8 --

def notTrue():
  x = (random.randint(1, 3))
  i01.mouth.speak("oh")
  #i01.mouth.speak(u"Ох")
  sleep(0.2)
  i01.mouth.speak("really")
  #i01.mouth.speak(u"действительно")
  fullspeed()
  i01.moveHead(16,11)
  i01.moveArm("left",60,67,67,40)
  i01.moveArm("right",5,116,10,28)
  i01.moveHand("left",143,69,48,2,2,23)
  i01.moveHand("right",89,60,78,43,68,163)
  i01.moveTorso(161,62,92)
  sleep(3)
  rest()
  sleep(1)
  relax()
  if x == 1:
    i01.mouth.speak("okay then, as you please")
    #i01.mouth.speak(u"Тогда, как вам угодно")
    i01.moveHead(90,90)
  if x == 2:
    i01.mouth.speak("oh, yes I forgot")
    #i01.mouth.speak(u"О, да, я забыл")
    i01.moveHead(90,90)
  if x == 3:
    i01.mouth.speak("oh, I will turn around")
    #i01.mouth.speak(u"О, я обернусь")
    i01.moveHead(90,90)
