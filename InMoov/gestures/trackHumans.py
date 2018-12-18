def trackHumans(noFaceRecognizerOverride=True):
  i01.cameraOn()
  i01.trackHumans()
  try:gui.setActiveTab("i01.opencv")
  except:pass
  i01.head.rollNeck.setOverrideAutoDisable(True)
  i01.head.rollNeck.moveToBlocking(90)
  i01.setHeadVelocity(-1,-1,-1,-1,-1)
  i01.headTracking.pid.setPID("x",12,5,0.1)
  i01.headTracking.pid.setPID("y",12,5,0.1)