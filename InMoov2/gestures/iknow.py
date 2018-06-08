
def iknow():
  x = (random.randint(1, 3))
  if x == 1:
    inMoov.mouth.speak("yes, me too")
	#inMoov.mouth.speak(u"Да, я тоже")
  if x == 2:
    inMoov.mouth.speak("I do too")
	#inMoov.mouth.speak(u"я тоже")
  if x == 3:
    inMoov.mouth.speak("sorry about that")
	#inMoov.mouth.speak(u"Извини за это")
