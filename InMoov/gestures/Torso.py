def Torso():
  i01.startedGesture()
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveTorso(60,90,90)
  sleep(2)
  i01.moveTorso(120,90,90)
  sleep(2)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.finishedGesture()

