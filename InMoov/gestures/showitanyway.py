def showitanyway():
  x = (random.randint(1, 3))
  if x == 1:
    i01.mouth.speak("as you please")
  if x == 2:
    i01.mouth.speak("i don't like that")
  if x == 3:
    i01.mouth.speak("alright")
  unhappy()
