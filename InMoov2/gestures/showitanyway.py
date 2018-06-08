
def showitanyway():
  x = (random.randint(1, 3))
  if x == 1:
    inMoov.mouth.speak("as you please")
	#inMoov.mouth.speak(u"как вам угодно")
  if x == 2:
    inMoov.mouth.speak("i don't like that")
	#inMoov.mouth.speak(u"Мне это не нравится")
  if x == 3:
    inMoov.mouth.speak("alright")
	#inMoov.mouth.speak(u"хорошо")
  unhappy()
