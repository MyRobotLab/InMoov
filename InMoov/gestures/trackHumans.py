def trackHumans(noFaceRecognizerOverride=True):
  stopTracking()
  i01.startHeadTracking("leftPort",12,13)
  #i01.startEyesTracking("leftPort",22,24)
  #i01.eyesTracking.pid.setPID("eyeX",eyeXPidKp,eyeXPidKi,eyeXPidKd)
  #i01.eyesTracking.pid.setPID("eyeY",eyeYPidKp,eyeYPidKi,eyeYPidKd)
  i01.headTracking.pid.setPID("x",rotheadPidKp,rotheadPidKi,rotheadPidKd)
  i01.headTracking.pid.setPID("y",neckPidKp,neckPidKi,neckPidKd)
  if noFaceRecognizerOverride:
    fr=i01.headTracking.faceDetect(faceRecognizerActivated)
    if faceRecognizerActivated:fr.train()# it takes some time to train and be able to recognize face
  else:
    i01.headTracking.faceDetect(False)
    # temporary disable "autoDisable"
  i01.head.rollNeck.setOverrideAutoDisable(True)
  i01.head.rollNeck.moveToBlocking(90)
