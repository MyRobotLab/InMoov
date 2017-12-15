def howmanyfingersdoihave():
  i01.startedGesture()
  fullspeed()
  i01.moveHead(49,74)
  i01.moveArm("left",75,83,79,24)
  i01.moveArm("right",65,82,71,24)
  i01.moveHand("left",74,140,150,157,168,92)
  i01.moveHand("right",89,80,98,120,114,0)
  sleep(2)
  i01.moveHand("right",0,80,98,120,114,0)
  i01.mouth.speakBlocking("10")

  sleep(.1)
  i01.moveHand("right",0,0,98,120,114,0)
  i01.mouth.speakBlocking("9")

  sleep(.1)
  i01.moveHand("right",0,0,0,120,114,0)
  i01.mouth.speakBlocking("8")

  sleep(.1)
  i01.moveHand("right",0,0,0,0,114,0)
  i01.mouth.speakBlocking("7")

  sleep(.1)
  i01.moveHand("right",0,0,0,0,0,0)
  i01.mouth.speakBlocking("6")

  sleep(.5)
  i01.setHeadSpeed(.70,.70)
  i01.moveHead(40,105)
  i01.moveArm("left",75,83,79,24)
  i01.moveArm("right",65,82,71,24)
  i01.moveHand("left",0,0,0,0,0,180)
  i01.moveHand("right",0,0,0,0,0,0)
  sleep(0.1)
  if Language=="fr":
    i01.mouth.speakBlocking("et 5 font 11")
  else:
    i01.mouth.speakBlocking("and five makes eleven")

  sleep(0.7)
  i01.setHeadSpeed(0.7,0.7)
  i01.moveHead(40,50)
  sleep(0.5)
  i01.setHeadSpeed(0.7,0.7)
  i01.moveHead(49,105)
  sleep(0.7)
  i01.setHeadSpeed(0.7,0.8)
  i01.moveHead(40,50)
  sleep(0.7)
  i01.setHeadSpeed(0.7,0.8)
  i01.moveHead(49,105)
  sleep(0.7)
  i01.setHeadSpeed(0.7,0.7)
  i01.moveHead(90,85)
  sleep(0.7)
  i01.mouth.speakBlocking("11")
  i01.moveArm("left",70,75,70,20)
  i01.moveArm("right",60,75,65,20)
  sleep(1)
  if Language=="fr":
    i01.mouth.speakBlocking("oupse, cela semble incorect, je vais reessayer")
  else:
    i01.mouth.speakBlocking("that doesn't seem right, I think I better try that again")


  i01.moveHead(40,105)
  i01.moveArm("left",75,83,79,24)
  i01.moveArm("right",65,82,71,24)
  i01.moveHand("left",140,168,168,168,158,90)
  i01.moveHand("right",87,138,109,168,158,25)
  sleep(2)

  i01.moveHand("left",10,140,168,168,158,90)
  i01.mouth.speakBlocking("1")
  sleep(.1)


  i01.moveHand("left",10,10,168,168,158,90)
  i01.mouth.speakBlocking("2")
  sleep(.1)

  i01.moveHand("left",10,10,10,168,158,90)
  i01.mouth.speakBlocking("3")
  sleep(.1)
  i01.moveHand("left",10,10,10,10,158,90)

  i01.mouth.speakBlocking("4")
  sleep(.1)
  i01.moveHand("left",10,10,10,10,10,90)

  i01.mouth.speakBlocking("5")
  sleep(.1)
  i01.setHeadSpeed(0.65,0.65)
  i01.moveHead(53,65)
  i01.moveArm("right",48,80,78,11)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.moveHand("left",10,10,10,10,10,90)
  i01.moveHand("right",10,10,10,10,10,25)
  sleep(1)
  if Language=="fr":
    i01.mouth.speakBlocking("et 5 font 10")
  else:
    i01.mouth.speakBlocking("and five makes ten")
  sleep(.5)
  if Language=="fr":
    i01.mouth.speakBlocking("c'est beaucoup mieux")
  else:
    i01.mouth.speakBlocking("it is better")
  i01.moveHead(95,85)
  i01.moveArm("left",75,83,79,24)
  i01.moveArm("right",40,70,70,10)
  sleep(0.5)
  if Language=="fr":
    i01.mouth.speakBlocking("inemouve a 10 doigts")
  else:
    i01.mouth.speakBlocking("inmoov has 10 fingers")
  sleep(0.5)
  i01.moveHead(90,90)
  i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
  i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
  i01.moveHand("left",140,140,140,140,140,60)
  i01.moveHand("right",140,140,140,140,140,60)
  sleep(1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.moveArm("left",5,90,30,11)
  i01.moveArm("right",5,90,30,11)
  sleep(0.5)
  i01.finishedGesture()
  relax()

