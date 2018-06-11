def howmanyfingersdoihave():
  inMoov.startedGesture()
  fullspeed()
  inMoov.moveHead(49,74)
  inMoov.moveArm("left",75,83,79,24)
  inMoov.moveArm("right",65,82,71,24)
  inMoov.moveHand("left",74,140,150,157,168,92)
  inMoov.moveHand("right",89,80,98,120,114,0)
  sleep(2)
  inMoov.moveHand("right",0,80,98,120,114,0)
  inMoov.mouth.speakBlocking("10")

  sleep(.1)
  inMoov.moveHand("right",0,0,98,120,114,0)
  inMoov.mouth.speakBlocking("9")

  sleep(.1)
  inMoov.moveHand("right",0,0,0,120,114,0)
  inMoov.mouth.speakBlocking("8")

  sleep(.1)
  inMoov.moveHand("right",0,0,0,0,114,0)
  inMoov.mouth.speakBlocking("7")

  sleep(.1)
  inMoov.moveHand("right",0,0,0,0,0,0)
  inMoov.mouth.speakBlocking("6")

  sleep(.5)
  inMoov.setHeadVelocity(.70,.70)
  inMoov.moveHead(40,105)
  inMoov.moveArm("left",75,83,79,24)
  inMoov.moveArm("right",65,82,71,24)
  inMoov.moveHand("left",0,0,0,0,0,180)
  inMoov.moveHand("right",0,0,0,0,0,0)
  sleep(0.1)
  if Language=="fr":
    inMoov.mouth.speakBlocking("et 5 font 11")
  else:
    inMoov.mouth.speakBlocking("and five makes eleven")

  sleep(0.7)
  inMoov.setHeadVelocity(26.0,26.0)
  inMoov.moveHead(40,50)
  sleep(0.5)
  inMoov.setHeadVelocity(26.0,26.0)
  inMoov.moveHead(49,105)
  sleep(0.7)
  inMoov.setHeadVelocity(26.0,36.0)
  inMoov.moveHead(40,50)
  sleep(0.7)
  inMoov.setHeadVelocity(26.0,36.0)
  inMoov.moveHead(49,105)
  sleep(0.7)
  inMoov.setHeadVelocity(26.0,26.0)
  inMoov.moveHead(90,85)
  sleep(0.7)
  inMoov.mouth.speakBlocking("11")
  inMoov.moveArm("left",70,75,70,20)
  inMoov.moveArm("right",60,75,65,20)
  sleep(1)
  if Language=="fr":
    inMoov.mouth.speakBlocking("oupse, cela semble incorect, je vais reessayer")
  else:
    inMoov.mouth.speakBlocking("that doesn't seem right, I think I better try that again")


  inMoov.moveHead(40,105)
  inMoov.moveArm("left",75,83,79,24)
  inMoov.moveArm("right",65,82,71,24)
  inMoov.moveHand("left",140,168,168,168,158,90)
  inMoov.moveHand("right",87,138,109,168,158,25)
  sleep(2)

  inMoov.moveHand("left",10,140,168,168,158,90)
  inMoov.mouth.speakBlocking("1")
  sleep(.1)


  inMoov.moveHand("left",10,10,168,168,158,90)
  inMoov.mouth.speakBlocking("2")
  sleep(.1)

  inMoov.moveHand("left",10,10,10,168,158,90)
  inMoov.mouth.speakBlocking("3")
  sleep(.1)
  inMoov.moveHand("left",10,10,10,10,158,90)

  inMoov.mouth.speakBlocking("4")
  sleep(.1)
  inMoov.moveHand("left",10,10,10,10,10,90)

  inMoov.mouth.speakBlocking("5")
  sleep(.1)
  inMoov.setHeadVelocity(22.0,22.0)
  inMoov.moveHead(53,65)
  inMoov.moveArm("right",48,80,78,11)
  inMoov.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.moveHand("left",10,10,10,10,10,90)
  inMoov.moveHand("right",10,10,10,10,10,25)
  sleep(1)
  if Language=="fr":
    inMoov.mouth.speakBlocking("et 5 font 10")
  else:
    inMoov.mouth.speakBlocking("and five makes ten")
  sleep(.5)
  if Language=="fr":
    inMoov.mouth.speakBlocking("c'est beaucoup mieux")
  else:
    inMoov.mouth.speakBlocking("it is better")
  inMoov.moveHead(95,85)
  inMoov.moveArm("left",75,83,79,24)
  inMoov.moveArm("right",40,70,70,10)
  sleep(0.5)
  if Language=="fr":
    inMoov.mouth.speakBlocking("inemouve a 10 doigts")
  else:
    inMoov.mouth.speakBlocking("inmoov has 10 fingers")
  sleep(0.5)
  inMoov.moveHead(90,90)
  inMoov.setHandVelocity("left", 36.0, 36.0, 36.0, 36.0, 36.0, 36.0)
  inMoov.setHandVelocity("right", 36.0, 36.0, 36.0, 36.0, 36.0, 36.0)
  inMoov.moveHand("left",140,140,140,140,140,60)
  inMoov.moveHand("right",140,140,140,140,140,60)
  sleep(-1)
  inMoov.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.moveArm("left",5,90,30,11)
  inMoov.moveArm("right",5,90,30,11)
  sleep(0.5)
  inMoov.finishedGesture()
  relax()

