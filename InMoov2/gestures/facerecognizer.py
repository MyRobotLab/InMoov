def facerecognizer():    
  #( tracking now use facerecognizer filter, this raw function is useful to learn faces, waiting "not identified person concept"  )
  if (inMoov.RobotIsTrackingSomething()):
    if inMoov.headTracking:inMoov.stopHeadTracking()
    if inMoov.eyesTracking:inMoov.eyesTracking.stopTracking()
  inMoov.opencv.capture()
  inMoov.opencv.addFilter("PyramidDown")
  fr=inMoov.opencv.addFilter("FaceRecognizer")
  inMoov.opencv.setDisplayFilter("FaceRecognizer")
  fr.train()# it takes some time to train and be able to recognize face