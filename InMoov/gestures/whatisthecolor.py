
def whatisthecolor():
  global coloring
  if coloring <= 2:
    inMoov.mouth.speak("I have no idea, I am not ready to recognize colors")
    #inMoov.mouth.speak(u"Я понятия не имею, я не готов распознавать цвета")
    coloring += 1
  elif coloring == 3:
    inMoov.mouth.speak("Sorry, I told you, I am not ready to recognize colors")
    #inMoov.mouth.speak(u"Извините, я же сказал, я не готов распознавать цвета")
    inMoov.moveArm("left",43,88,22,10)
    inMoov.moveArm("right",20,90,30,10)
    inMoov.moveHand("left",0,0,0,0,0,119)
    inMoov.moveHand("right",0,0,0,0,0,119)
    sleep(2)
    relax()
    coloring += 1
  elif coloring == 4:
    inMoov.mouth.speak("Gael, you are annoying, stop asking me about the colors")
    #inMoov.mouth.speak(u"Гаэль, ты раздражаешь, перестань спрашивать меня о цветах")
    inMoov.moveArm("left",30,83,22,10)
    inMoov.moveArm("right",40,85,30,10)
    inMoov.moveHand("left",130,180,180,180,180,119)
    inMoov.moveHand("right",130,180,180,180,180,119)
    sleep(2)
    relax()
    coloring += 1
  elif coloring == 5:
    inMoov.setHeadVelocity(59, 59, 50, 50, -1)
    inMoov.moveHead(80,66)
    sleep(1)
    inMoov.setHeadVelocity(59, 59, 50, 50, -1)
    inMoov.moveHead(80,110)
    sleep(1)
    inMoov.setHeadVelocity(59, 59, 50, 50, -1)
    inMoov.moveHead(80,66)
    sleep(1)
    inMoov.setHeadVelocity(59, 59, 50, 50, -1)
    inMoov.moveHead(80,110)
    sleep(1)
    inMoov.setHeadVelocity(59, 59, 50, 50, -1)
    inMoov.moveHead(80,66)
    sleep(1)
    inMoov.mouth.speak("Humans are worst than robots, don't they ever learn")
    #inMoov.mouth.speak(u"Люди хуже, чем роботы, разве они никогда не учатся")
    fullspeed()
    inMoov.moveArm("left",85,106,25,18)
    inMoov.moveArm("right",87,107,32,18)
    inMoov.moveHand("left",110,62,56,88,81,145)
    inMoov.moveHand("right",78,88,101,95,81,27)
    inMoov.moveTorso(90,90,90)
    sleep(4)
    relax()
    coloring += 1
