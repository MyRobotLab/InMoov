def whoisthis(name):
  if isNeopixelActivated==1:
    i01.setNeopixelAnimation("Color Wipe", 100, 5, 10, 15) 
  if isChatbotActivated:
    i01.cameraOn()
    fr=i01.vision.setActiveFilter("FaceRecognizer")
    # set the name on the filter that will be used for the saved examples
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
    fr.train#Name = name
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
    sleep(6)
    onRecognizedFace(name)
