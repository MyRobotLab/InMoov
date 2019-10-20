def lookaroundyou():
  i01.setHeadVelocity(80, 80, 50, 50, -1)
  i01.mouth.speak("ok you have my attention")
  for x in range(0, 1):
    x = (random.randint(1, 6))
    if x == 1:
      i01.head.neck.moveTo(90)
      eyeslooking()
    if x == 2:
      i01.head.rothead.moveTo(80)
      eyeslooking()
    if x == 3:
      headdown()
      eyeslooking()
    if x == 4:
      headupp()
      eyeslooking()
    if x == 5:
      headright()
      eyeslooking()
    if x == 6:
      headleft()
      eyeslooking()
    sleep(1)
    x = (random.randint(1, 4))
    if x == 1:
      i01.mouth.speak("looking nice")
    if x == 2:
      i01.mouth.speak("i like it here")
    if x == 3:
      i01.mouth.speak("can I help you")
    if x == 4:
      i01.mouth.speak("what would you like to do")
    relax()
