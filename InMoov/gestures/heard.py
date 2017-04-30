def heard(data):
  global walkingThread

  print("Heard Called :" + str(data))

  if (data == "hi there"):
    lookaroundyou(data)

  if (data == "are you alright"):
    x = (random.randint(1, 2))
    i01.setHeadSpeed(0.85,1.0,0.85,0.85,1.0)
    i01.moveHead(90,60,90,180,65)
    sleep(1)
    i01.moveHead(90,120,90,180,65)
    sleep(1)
    i01.moveHead(90,60,90,180,65)
    sleep(1)
    i01.moveHead(90,120,90,180,65)
    sleep(1)
    i01.moveHead(90,90,90,180,65)
    sleep(1)
    if x == 1:
      i01.mouth.speak("i am very, super, mega bored")
      i01.moveArm("left",85,93,42,16)
      i01.moveArm("right",87,93,37,18)
      i01.moveHand("left",124,82,65,81,41,143)
      i01.moveHand("right",59,53,89,61,36,21)
      i01.moveTorso(90,90,90)
      sleep(0.2)
      i01.setHeadSpeed(1.0,1.0,1.0,1.0,1.0)
      i01.moveHead(90,90,90,90,65)
      sleep(1)
      relax()
    if x == 2:
      i01.mouth.speak("I feel like a machine, doing the same thing over and over")
      i01.moveArm("left",85,93,42,16)
      i01.moveArm("right",87,93,37,18)
      i01.moveHand("left",124,82,65,81,41,143)
      i01.moveHand("right",59,53,89,61,36,21)
      i01.moveTorso(90,90,90)
      sleep(0.2)
      i01.setHeadSpeed(1.0,1.0,1.0,1.0,1.0)
      i01.moveHead(90,90,90,90,65)
      sleep(1)
      relax()

  if (data == "you did great"):
    perfect()

  if (data == "show your back"):
    i01.mouth.speak("you know I don't like to show my back because it is not finished")

  if (data == "not true it's finished"):
    x = (random.randint(1, 3))
    i01.mouth.speak("oh")
    forwardServo.attach()
    directionServo.moveTo(45)
    forwardServo.moveTo(60)
    sleep(0.2)
    i01.mouth.speak("really")
    forwardServo.disable()
    fullspeed()
    i01.moveHead(16,11)
    i01.moveArm("left",60,67,67,40)
    i01.moveArm("right",5,116,10,28)
    i01.moveHand("left",143,69,48,2,2,23)
    i01.moveHand("right",89,60,78,43,68,163)
    i01.moveTorso(161,62,92)
    sleep(3)
    rest()
    sleep(1)
    relax()
    if x == 1:
      i01.mouth.speak("okay then, as you please")
      i01.moveHead(90,90)
    if x == 2:
      i01.mouth.speak("oh, yes I forgot")
      i01.moveHead(90,90)
    if x == 3:
      i01.mouth.speak("oh, I will turn around")
      i01.moveHead(90,90)

  if (data == "it's an object"):
    i01.mouth.speak("definition of an object, anything that is visible or tangible and relatively stable in form. ")


  if (data == "i know but show it anyway"):
    x = (random.randint(1, 3))
    if x == 1:
      i01.mouth.speak("as you please")
    if x == 2:
      i01.mouth.speak("i don't like that")
    if x == 3:
      i01.mouth.speak("alright")
    unhappy()

  if (data == "sorry i forgot"):
    x = (random.randint(1, 2))
    if x == 1:
      i01.mouth.speak("that's alright")
    if x == 2:
      i01.mouth.speak("you forget all the time")

  if (data == "it's okay"):
    i01.mouth.speak("good")


  if (data == "very good, thank you"):
    i01.mouth.speak("okay, good")

  if (data == "look at the people"):
    i01.setHeadSpeed(0.8, 0.8)
    for y in range(0, 10):
      x = (random.randint(1, 5))
      if x == 1:
        fullspeed()
        i01.head.neck.moveTo(90)
        eyeslooking(data)
        sleep(2)
        trackHumans()
        sleep(10)
        stopTracking()
      if x == 2:
        fullspeed()
        i01.head.rothead.moveTo(80)
        eyeslooking(data)
        sleep(2)
        trackHumans()
        sleep(10)
        stopTracking()
      if x == 3:
        fullspeed()
        headdown()
        sleep(1)
        trackHumans()
        sleep(10)
        stopTracking()
      if x == 4:
        fullspeed()
        lookrightside()
        sleep(2)
        trackHumans()
        sleep(10)
        stopTracking()
      if x == 5:
        fullspeed()
        lookleftside()
        sleep(2)
        trackHumans()
        sleep(10)
        stopTracking()
    sleep(1)
    lookinmiddle()
    sleep(3)
    i01.mouth.speak("nice to meet you all")

  if (data == "take a look around"):
    lookaroundyou()

  if (data == "good morning"):
    i01.mouth.speak("good morning")
    x = (random.randint(1, 4))
    if x == 1:
      i01.mouth.speak("i hope you had a good night sleep")
    if x == 2:
      i01.mouth.speak("nice to see you again")
    if x == 3:
      i01.mouth.speak("this is going to be a good day")

  if (data == "very good"):
    i01.mouth.speak("thanks")

  if (data =="italian hello"):
    italianhello()

  #if (data =="finnish hello"):
    #finnishhello()

  if (data =="do you like to eat indian food "):
    fullspeed()
    i01.setHeadSpeed(0.85, 0.80, 0.90, 0.90, 1.0)
    i01.moveHead(60,40,7,85,52)
    sleep(1)
    i01.moveHead(80,40,7,85,52)
    sleep(2)
    i01.setHeadSpeed(0.92, 0.80, 0.90, 0.90, 1.0)
    i01.moveHead(100,40,7,85,52)
    sleep(0.4)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    i01.moveHead(80,40,7,85,52)
    i01.mouth.speakBlocking("yes, i want some paneer tikka")
    sleep(1)
    i01.moveHead(60,90,80,90,52)
    sleep(0.8)
    relax()

  if (data =="do you speak hindi"):
    i01.mouth.speak("yes, i can speak any language")
    i01.moveHead(116,80)
    i01.moveArm("left",85,93,42,16)
    i01.moveArm("right",87,93,37,18)
    i01.moveHand("left",124,82,65,81,41,143)
    i01.moveHand("right",59,53,89,61,36,21)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    sleep(1)
    relax()

  if (data == "where are you from"):
    phonehome()

  if (data == "i know"):
    x = (random.randint(1, 3))
    if x == 1:
      i01.mouth.speak("yes, me too")
    if x == 2:
      i01.mouth.speak("I do too")
    if x == 3:
      i01.mouth.speak("sorry about that")

  if (data == "sorry"):
    x = (random.randint(1, 3))
    if x == 1:
      i01.mouth.speak("no problems")
    if x == 2:
      i01.mouth.speak("it doesn't matter")
    if x == 3:
      i01.mouth.speak("it's okay")

  if (data == "nice"):
    x = (random.randint(1, 3))
    if x == 1:
      i01.mouth.speak("I know")
    if x == 2:
      i01.mouth.speak("yes, indeed")
    if x == 3:
      i01.mouth.speak("you are damn right")

  if (data == "hello"):
    hello()
    relax()

  if (data == "bye bye"):
    i01.mouth.speak("see you soon")
    global helvar
    helvar = 1
    x = (random.randint(1, 2))
    if x == 1:
      i01.mouth.speak("i'm looking forward to see you again")
    if x == 2:
      i01.mouth.speak("goodbye")

  if (data == "thank you"):
    x = (random.randint(1, 3))
    if x == 1:
      i01.mouth.speak("you are welcome")
    if x == 2:
      i01.mouth.speak("my pleasure")
    if x == 3:
      i01.mouth.speak("it's okay")

  if (data == "thanks"):
    x = (random.randint(1, 2))
    if x == 1:
      i01.mouth.speak("it's okay")
    if x == 2:
      i01.mouth.speak("sure")

  if (data == "go forward"):
      #forwardServo.moveTo(60)
      # only start back up if we haven't already started.
      if not walkingThread.running:
        walkingThread.start()

  if (data == "walk gesture"):
      for _ in itertools.repeat(None):
        fullspeed()
        relax()
        sleep(1)
        rest()
      #i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      #i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      #i01.setArmSpeed("right", 0.95, 0.95, 0.95, 0.85)
      #i01.setArmSpeed("left", 0.95, 0.95, 0.95, 0.85)
      #i01.setHeadSpeed(0.75, 0.75)
      #i01.moveHead(70,79,85,85,65)
      #i01.moveArm("left",5,90,10,10)
      #i01.moveArm("right",15,90,40,10)
      #i01.moveHand("left",92,33,37,71,66,10)
      #i01.moveHand("right",81,66,82,60,105,100)
      #i01.moveTorso(75,97,90)
      #sleep(1)
      #i01.moveHead(79,100,85,85,65)
      #i01.moveArm("left",15,84,43,15)
      #i01.moveArm("right",5,82,10,20)
      #i01.moveHand("left",92,33,37,71,66,50)
      #i01.moveHand("right",81,66,82,60,105,150)
      #i01.moveTorso(124,83,90)
        sleep(1)

  if (data == "go backwards"):
      forwardServo.moveTo(110)
      relax()

  if (data == "watch out and stop"):
      walkingThread.running = False
      forwardServo.moveTo(93)
      # join the thread / let it stop
      walkingThread.join()
      # create a new one
      walkingThread = WalkingThread(i01, forwardServo)
      try:
        relax()
      except:
        print "It's difficult to relax..."

  if (data == "walking off"):
      walkingThread.running = False
      # join the thread / let it stop
      walkingThread.join()
      # create a new one
      walkingThread = WalkingThread(i01, forwardServo)
      try:
        relax()
      except:
        print "It's difficult to relax..."



  if (data == "to the left"):
      directionServo.moveTo(135)
      i01.setHeadSpeed(0.75, 0.75)
      i01.moveHead(70,124)

  if (data == "to the right"):
      directionServo.moveTo(45)
      i01.setHeadSpeed(0.75, 0.75)
      i01.moveHead(70,63)

  if (data == "go straight"):
      directionServo.moveTo(83)
      i01.setHeadSpeed(0.75, 0.75)
      i01.moveHead(70,80)

  if (data == "disconnect wheel"):
      directionServo.disable()
      forwardServo.disable()
  if (data == "attach wheel"):
      directionServo.attach()
      forwardServo.attach()

  if (data == "how do you do"):
    if helvar <= 2:
      i01.mouth.speak("I'm fine thank you")
      global helvar
      helvar += 1
    elif helvar == 3:
      i01.mouth.speak("you have already said that at least twice")
      i01.moveArm("left",43,88,22,10)
      i01.moveArm("right",20,90,30,10)
      i01.moveHand("left",0,0,0,0,0,119)
      i01.moveHand("right",0,0,0,0,0,119)
      sleep(2)
      relax()
      global helvar
      helvar += 1
    elif helvar == 4:
      i01.mouth.speak("what is your problem stop saying how do you do all the time")
      i01.moveArm("left",30,83,22,10)
      i01.moveArm("right",40,85,30,10)
      i01.moveHand("left",130,180,180,180,180,119)
      i01.moveHand("right",130,180,180,180,180,119)
      sleep(2)
      relax()
      global helvar
      helvar += 1
    elif helvar == 5:
      i01.mouth.speak("i will ignore you if you say how do you do one more time")
      unhappy()
      sleep(4)
      relax()
      global helvar
      helvar += 1

  if (data == "i love you"):
    i01.mouth.speak("i love you too")
    i01.moveHead(116,80)
    i01.moveArm("left",85,93,42,16)
    i01.moveArm("right",87,93,37,18)
    i01.moveHand("left",124,82,65,81,41,143)
    i01.moveHand("right",59,53,89,61,36,21)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    sleep(1)
    relax()

  if (data == "what is the weather"):
    global weathervar
    if weathervar <= 2:
      i01.mouth.speak("I have no idea, I am not connected to internet")
      weathervar += 1
    elif weathervar == 3:
      i01.mouth.speak("Sorry, I told you, I am not connected to internet")
      i01.moveArm("left",43,88,22,10)
      i01.moveArm("right",20,90,30,10)
      i01.moveHand("left",0,0,0,0,0,119)
      i01.moveHand("right",0,0,0,0,0,119)
      sleep(2)
      relax()
      weathervar += 1
    elif weathervar == 4:
      i01.mouth.speak("Gael, you are annoying, stop asking me the weather")
      i01.moveArm("left",30,83,22,10)
      i01.moveArm("right",40,85,30,10)
      i01.moveHand("left",130,180,180,180,180,119)
      i01.moveHand("right",130,180,180,180,180,119)
      sleep(2)
      relax()
      weathervar += 1
    elif weathervar == 5:
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
      i01.mouth.speak("Well, well, Humans are worst than robots, they never learn")
      fullspeed()
      i01.moveArm("left",85,106,25,18)
      i01.moveArm("right",87,107,32,18)
      i01.moveHand("left",110,62,56,88,81,145)
      i01.moveHand("right",78,88,101,95,81,27)
      i01.moveTorso(90,90,90)
      sleep(4)
      relax()
      weathervar += 1





