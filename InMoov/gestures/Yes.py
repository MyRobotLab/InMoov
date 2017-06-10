def Yes():
  i01.disableRobotCanMoveHeadRandom(30)
  
  if isHeadActivated==1:
    i01.setHeadVelocity(40,40,40)
    i01.moveHead(130,90)
    sleep(0.5)
    i01.moveHead(50,93)
    sleep(0.8)
    i01.moveHead(130,90)
    sleep(0.8)
    i01.moveHead(60,91)
    sleep(0.8)
    i01.moveHead(120,88)
    sleep(0.8)
    i01.moveHead(70,90)
    sleep(0.5)
    i01.moveHead(90,90)

  
