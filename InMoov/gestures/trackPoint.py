def trackPoint():
  i01.cameraOn()
  i01.trackPoint()
  try:gui.setActiveTab("i01.opencv")
  except:pass
  i01.head.rollNeck.setOverrideAutoDisable(True)
  i01.head.rollNeck.moveToBlocking(90)
  i01.setHeadSpeed(100.0,100.0,100.0,100.0,100.0)
  i01.headTracking.pid.setPID("x",12,5,0.1)
  i01.headTracking.pid.setPID("y",12,5,0.1)