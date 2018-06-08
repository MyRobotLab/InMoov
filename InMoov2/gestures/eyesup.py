def eyesup():
  inMoov.startedGesture()
  inMoov.head.eyeY.moveTo(0)
  sleep(1)
  inMoov.finishedGesture()

