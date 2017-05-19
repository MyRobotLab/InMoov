def rockpaperscissors2(data):
  x = (random.randint(1, 3))
  if x == 1:
    ready()
    sleep(2)
    rock()
    sleep(2)
    if (data == "i have rock"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("zero zero")
      if x == 2:
        i01.mouth.speak("no no")
      if x == 3:
        i01.mouth.speak("no points")
      sleep(1)
    if (data == "i have paper"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("paper beats rock")
      if x == 2:
        i01.mouth.speak("your point")
      if x == 3:
        i01.mouth.speak("you got this one")
      human += 1
      sleep(1)
    if (data == "i have scissors"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("1 point for me")
      if x == 2:
        i01.mouth.speak("going fine")
      if x == 3:
        i01.mouth.speak("rock beats scissors")
      inmoov += 1
      sleep(1)


  if x == 2:
    ready()
    sleep(2)
    paper()
    sleep(2)
    if (data == "i have rock"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("1 point")
      if x == 2:
        i01.mouth.speak("paper beats rock")
      if x == 3:
        i01.mouth.speak("my point")
      inmoov += 1
      sleep(1)
    if (data == "i have paper"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("no points")
      if x == 2:
        i01.mouth.speak("ok lets try again")
        sleep(2)
      if x == 3:
        i01.mouth.speak("again")
      sleep(1)
    if (data == "i have scissors"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("oh no you get 1 point")
      if x == 2:
        i01.mouth.speak("this is not good for me")
      if x == 3:
        i01.mouth.speak("your point")
      human += 1
      sleep(1)

  if x == 3:
    ready()
    sleep(2)
    scissors()
    sleep(2)
    if (data == "i have rock"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("oh no")
      if x == 2:
        i01.mouth.speak("rock beats scissors")
      if x == 3:
        i01.mouth.speak("i feel generous today")
      human += 1
      sleep(1)
    if (data == "i have paper"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("i've got you")
      if x == 2:
        i01.mouth.speak("my point")
      if x == 3:
        i01.mouth.speak("good")
      inmoov += 1
      sleep(1)
    if (data == "i have scissors"):
      x = (random.randint(1, 3))
      if x == 1:
        i01.mouth.speak("no no")
      if x == 2:
        i01.mouth.speak("zero zero")
      if x == 3:
        i01.mouth.speak("no points")
      sleep(1)
  if inmoov == 3:
    stoprockpaperscissors()
    sleep(1)
  elif human == 3:             # changed from if to  elif
    stoprockpaperscissors()
    sleep(1)
  elif inmoov <= 2:            # changed from if to  elif
    rockpaperscissors2(data)
  elif human <= 2:             # changed from if to  elif
    rockpaperscissors2(data)

