def eyesleft():
  inMoov.startedGesture()
  inMoov.head.eyeX.moveTo(180)
  sleep(1)
  inMoov.finishedGesture()

