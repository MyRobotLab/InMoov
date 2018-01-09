# -- coding: utf-8 --

def whatisthecolor():
  global coloring
  if coloring <= 2:
    i01.mouth.speak("I have no idea, I am not ready to recognize colors")
    #i01.mouth.speak(u"Я понятия не имею, я не готов распознавать цвета")
    coloring += 1
  elif coloring == 3:
    i01.mouth.speak("Sorry, I told you, I am not ready to recognize colors")
    #i01.mouth.speak(u"Извините, я же сказал, я не готов распознавать цвета")
    i01.moveArm("left",43,88,22,10)
    i01.moveArm("right",20,90,30,10)
    i01.moveHand("left",0,0,0,0,0,119)
    i01.moveHand("right",0,0,0,0,0,119)
    sleep(2)
    relax()
    coloring += 1
  elif coloring == 4:
    i01.mouth.speak("Gael, you are annoying, stop asking me about the colors")
    #i01.mouth.speak(u"Гаэль, ты раздражаешь, перестань спрашивать меня о цветах")
    i01.moveArm("left",30,83,22,10)
    i01.moveArm("right",40,85,30,10)
    i01.moveHand("left",130,180,180,180,180,119)
    i01.moveHand("right",130,180,180,180,180,119)
    sleep(2)
    relax()
    coloring += 1
  elif coloring == 5:
    i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
    i01.moveHead(80,66)
    sleep(1)
    i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
    i01.moveHead(80,110)
    sleep(1)
    i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
    i01.moveHead(80,66)
    sleep(1)
    i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
    i01.moveHead(80,110)
    sleep(1)
    i01.setHeadSpeed(0.95, 0.95, 0.90, 0.90, 1.0)
    i01.moveHead(80,66)
    sleep(1)
    i01.mouth.speak("Humans are worst than robots, don't they ever learn")
    #i01.mouth.speak(u"Люди хуже, чем роботы, разве они никогда не учатся")
    fullspeed()
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(4)
    relax()
    coloring += 1
