def LookAtTheSky():
  i01.disableRobotCanMoveHeadRandom(30)
  i01.setHeadVelocity(30,30)
  i01.moveHead(180,90)
  sleep(5)
  i01.setHeadVelocity(20, 20)
  i01.moveHead(90,90)
  