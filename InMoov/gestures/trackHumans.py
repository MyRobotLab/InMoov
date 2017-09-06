def trackHumans():
  i01.startedGesture()
  if (i01.RobotIsOpenCvCapturing()):
    i01.opencv.removeFilter("Gray")
    i01.opencv.removeFilter("PyramidDown")
    i01.opencv.removeFilter("FaceRecognizer")
    i01.startHeadTracking("leftPort",12,13)
    #i01.startEyesTracking("leftPort",22,24)
    sleep(1)
    i01.headTracking.faceDetect()
    #i01.eyesTracking.faceDetect()
    i01.setHeadVelocity(80, -1)
    sleep(1)
    fullspeed()
    
  else:
    i01.startHeadTracking("leftPort",12,13)
    #i01.startEyesTracking("leftPort",22,24)
    sleep(1)
    i01.headTracking.faceDetect()
    #i01.eyesTracking.faceDetect()
    i01.setHeadVelocity(80, -1)
    sleep(1)
    fullspeed()
  i01.finishedGesture()

