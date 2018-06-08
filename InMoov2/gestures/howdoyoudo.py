
def howdoyoudo():
  global helvar
  if helvar <= 2:
    inMoov.mouth.speak("I'm fine thank you")
    #inMoov.mouth.speak(u"Я в порядке, спасибо")
    helvar += 1
  elif helvar == 3:
    inMoov.mouth.speak("you have already said that at least twice")
    #inMoov.mouth.speak(u"Вы уже сказали, это по крайней мере дважды")
    inMoov.moveArm("left",43,88,22,10)
    inMoov.moveArm("right",20,90,30,10)
    inMoov.moveHand("left",0,0,0,0,0,119)
    inMoov.moveHand("right",0,0,0,0,0,119)
    sleep(2)
    relax()
    helvar += 1
  elif helvar == 4:
    inMoov.mouth.speak("what is your problem stop saying how do you do all the time")
    #inMoov.mouth.speak(u"В чем ваша проблема перестает говорить, как дела")
    inMoov.moveArm("left",30,83,22,10)
    inMoov.moveArm("right",40,85,30,10)
    inMoov.moveHand("left",130,180,180,180,180,119)
    inMoov.moveHand("right",130,180,180,180,180,119)
    sleep(2)
    relax()
    helvar += 1
  elif helvar == 5:
    inMoov.mouth.speak("i will ignore you if you say how do you do one more time")
    #inMoov.mouth.speak(u"Я проигнорирую вас, если вы скажете еще раз, как дела ")
    unhappy()
    sleep(4)
    relax()
    helvar += 1
