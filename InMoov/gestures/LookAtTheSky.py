def LookAtTheSky():
  global MoveHeadRandom
  MoveHeadRandom=0
  i01.setHeadSpeed(0.2, 0.2)
  i01.moveHead(0,90)
  sleep(5)
  i01.setHeadSpeed(0.1, 0.1)
  i01.moveHead(90,90)