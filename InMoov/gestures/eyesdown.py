def eyesdown():
  inMoov.startedGesture()
  inMoov.head.eyeY.moveTo(180)
  sleep(1)
  inMoov.finishedGesture()

