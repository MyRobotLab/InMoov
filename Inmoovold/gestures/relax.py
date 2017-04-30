def relax():
  PlayNeopixelAnimation("Color Wipe", 0, 0, 20, 1)
  sleep(2)
  PlayNeopixelAnimation("Ironman", 0, 0, 255, 1)
  if (i01.eyesTracking.getOpenCV().capturing):
    global RobotCanMoveHeadWhileSpeaking
    RobotCanMoveHeadWhileSpeaking=0
    i01.setHandVelocity("left", 43, 43, 43, 43, 43, 43)
    i01.setHandVelocity("right", 43, 43, 43, 43, 43, 43)
    i01.setArmVelocity("right", 31, 43, 23, 43)
    i01.setArmVelocity("left", 60, 23, 31, 31)
    #i01.setHeadSpeed(43, 43)
    i01.setTorsoVelocity(31, 16, -1)
    #i01.moveHead(79,100)
    i01.moveArm("left",5,84,28,12)
    i01.moveArm("right",5,82,28,12)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(95,90,90)

  else:
    global RobotCanMoveHeadWhileSpeaking
    RobotCanMoveHeadWhileSpeaking=1
    i01.setHandVelocity("left", 43, 43, 43, 43, 43, 43)
    i01.setHandVelocity("right", 43, 43, 43, 43, 43, 43)
    i01.setArmVelocity("right", 31, 43, 23, 43)
    i01.setArmVelocity("left", 60, 23, 31, 31)
    i01.setHeadVelocity(43, 43)
    i01.setTorsoVelocity(31, 16, -1)
    i01.moveHead(79,100)
    i01.moveArm("left",5,84,28,12)
    i01.moveArm("right",5,82,28,12)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(95,90,90)
