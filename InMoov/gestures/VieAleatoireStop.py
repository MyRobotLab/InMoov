def VieAleatoireStop():
  MoveHeadTimer.stopClock()
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  MoveBodyTimer.stopClock()
  global MoveBodyRandom
  MoveBodyRandom=0

  