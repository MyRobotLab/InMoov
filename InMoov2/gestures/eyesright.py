def eyesright():
  inMoov.startedGesture()
  inMoov.head.eyeX.moveTo(0)
  sleep(1)
  inMoov.finishedGesture()

