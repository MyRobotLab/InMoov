def relax():
  neopixel.setAnimation("Color Wipe", 0, 0, 20, 1)
  sleep(2)
  neopixel.setAnimation("Ironman", 0, 0, 255, 1)
  if (i01.eyesTracking.getOpenCV().capturing):
    global MoveBodyRandom
    MoveBodyRandom=0
    global MoveHeadRandom
    MoveHeadRandom=0
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
    i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
    i01.setHeadSpeed(0.85, 0.85)
    i01.setTorsoSpeed(0.75, 0.55, 1.0)
    i01.moveHead(79,100)
    i01.moveArm("left",5,84,28,14)
    i01.moveArm("right",5,82,28,16)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(95,90,90)

  else:
    global MoveBodyRandom
    MoveBodyRandom=1
    global MoveHeadRandom
    MoveHeadRandom=1
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
    i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
    i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
    i01.setHeadSpeed(0.85, 0.85)
    i01.setTorsoSpeed(0.75, 0.55, 1.0)
    #i01.moveHead(79,100)
    i01.moveArm("left",5,84,28,14)
    i01.moveArm("right",5,82,28,16)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(95,90,90)


