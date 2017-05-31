def tiltHeadAgree():
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  i01.setHeadVelocity(60, 60, 60)
  i01.moveHead(110,90,180)
  sleep(0.5)
  i01.moveHead(90,90,90)
