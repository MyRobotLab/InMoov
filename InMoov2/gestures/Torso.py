def Torso():
  inMoov.startedGesture()
  inMoov.setTorsoVelocity(-1, -1, -1)
  inMoov.moveTorso(60,90,90)
  sleep(2)
  inMoov.moveTorso(120,90,90)
  sleep(2)
  inMoov.moveTorso(90,90,90)
  sleep(2)
  inMoov.finishedGesture()

