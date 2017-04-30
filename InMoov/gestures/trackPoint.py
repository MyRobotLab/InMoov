def trackPoint():
  global RobotCanMoveHeadWhileSpeaking
  RobotCanMoveHeadWhileSpeaking=0
  i01.headTracking.startLKTracking()
  i01.eyesTracking.startLKTracking()
  i01.setHeadVelocity(80, -1)
  sleep(1)
  fullspeed()
