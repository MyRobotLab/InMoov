# -- coding: utf-8 --

def howdoyoudo():
  global helvar
  if helvar <= 2:
    i01.mouth.speak("I'm fine thank you")
    #i01.mouth.speak(u"Я в порядке, спасибо")
    helvar += 1
  elif helvar == 3:
    i01.mouth.speak("you have already said that at least twice")
    #i01.mouth.speak(u"Вы уже сказали, это по крайней мере дважды")
    i01.moveArm("left",43,88,22,10)
    i01.moveArm("right",20,90,30,10)
    i01.moveHand("left",0,0,0,0,0,119)
    i01.moveHand("right",0,0,0,0,0,119)
    sleep(2)
    relax()
    helvar += 1
  elif helvar == 4:
    i01.mouth.speak("what is your problem stop saying how do you do all the time")
    #i01.mouth.speak(u"В чем ваша проблема перестает говорить, как дела")
    i01.moveArm("left",30,83,22,10)
    i01.moveArm("right",40,85,30,10)
    i01.moveHand("left",130,180,180,180,180,119)
    i01.moveHand("right",130,180,180,180,180,119)
    sleep(2)
    relax()
    helvar += 1
  elif helvar == 5:
    i01.mouth.speak("i will ignore you if you say how do you do one more time")
    #i01.mouth.speak(u"Я проигнорирую вас, если вы скажете еще раз, как дела ")
    unhappy()
    sleep(4)
    relax()
    helvar += 1
