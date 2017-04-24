def trackHumans():
  global MoveBodyRandom
  MoveBodyRandom=0
  global MoveHeadRandom
  MoveHeadRandom=0
  i01.headTracking.faceDetect()
  i01.eyesTracking.faceDetect()
  fullspeed()

