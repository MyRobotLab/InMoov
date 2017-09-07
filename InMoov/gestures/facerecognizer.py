def facerecognizer():
    
  i01.startedGesture()
  if (i01.RobotIsTrackingSomething()):
    i01.headTracking.stopTracking()
    i01.eyesTracking.stopTracking()
    i01.opencv.addFilter("PyramidDown")
    i01.opencv.setDisplayFilter("FaceRecognizer")
    fr=i01.opencv.addFilter("FaceRecognizer")
    fr.train()# it takes some time to train and be able to recognize face
    #if((lastName+"-inmoovWebKit" not in inmoovWebKit.getSessionNames())):
        #mouth.speak("Hello "+lastName)
        #sleep(2)
    #inmoovWebKit.getResponse(lastName,data)

  else:
    i01.opencv.capture()
    i01.opencv.addFilter("PyramidDown")
    i01.opencv.setDisplayFilter("FaceRecognizer")
    fr=i01.opencv.addFilter("FaceRecognizer")
    fr.train()# it takes some time to train and be able to recognize face
    #if((lastName+"-inmoovWebKit" not in inmoovWebKit.getSessionNames())):
        #mouth.speak("Hello "+lastName)
        #sleep(2)
    #inmoovWebKit.getResponse(lastName,data)
  i01.finishedGesture()
