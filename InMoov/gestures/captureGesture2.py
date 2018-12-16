def captureGesture2():
  RobotCanMoveHeadWhileSpeaking=False
  i01.mouth.speakBlocking("I am capturing this gesture")
  i01.captureGesture()
  RobotCanMoveHeadWhileSpeaking=True
