def facerecognizer():    
  #( tracking now use facerecognizer filter, this raw function is useful to learn faces, waiting "not identified person concept"  )
  if (i01.RobotIsTrackingSomething()):
    if i01.headTracking:i01.stopHeadTracking()
    if i01.eyesTracking:i01.eyesTracking.stopTracking()
  i01.opencv.capture()
  i01.opencv.addFilter("PyramidDown")
  fr=i01.opencv.addFilter("FaceRecognizer")
  i01.opencv.setDisplayFilter("FaceRecognizer")
  fr.train()# it takes some time to train and be able to recognize face