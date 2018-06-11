def trackHumans(noFaceRecognizerOverride=True):
  stopTracking()
  inMoov.startHeadTracking("leftPort",12,13)
  #inMoov.startEyesTracking("leftPort",22,24)
  #inMoov.eyesTracking.pid.setPID("eyeX",eyeXPidKp,eyeXPidKi,eyeXPidKd)
  #inMoov.eyesTracking.pid.setPID("eyeY",eyeYPidKp,eyeYPidKi,eyeYPidKd)
  inMoov.headTracking.pid.setPID("x",rotheadPidKp,rotheadPidKi,rotheadPidKd)
  inMoov.headTracking.pid.setPID("y",neckPidKp,neckPidKi,neckPidKd)
  if noFaceRecognizerOverride:
    fr=inMoov.headTracking.faceDetect(faceRecognizerActivated)
    if faceRecognizerActivated:fr.train()# it takes some time to train and be able to recognize face
  else:
    inMoov.headTracking.faceDetect(False)
    # temporary disable "autoDisable"
  inMoov.head.rollNeck.setOverrideAutoDisable(True)
  inMoov.head.rollNeck.moveToBlocking(90)
