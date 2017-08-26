# -- coding: utf-8 --

def showitanyway():
  x = (random.randint(1, 3))
  if x == 1:
    i01.mouth.speak("as you please")
	#i01.mouth.speak(u"как вам угодно")
  if x == 2:
    i01.mouth.speak("i don't like that")
	#i01.mouth.speak(u"Мне это не нравится")
  if x == 3:
    i01.mouth.speak("alright")
	#i01.mouth.speak(u"хорошо")
  unhappy()
