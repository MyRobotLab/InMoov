from org.myrobotlab.opencv import OpenCVFilterFaceRecognizer
def memorizePerson():
  i01.chatBot.getResponse("SAY " + "What name should I memorize for this person")

def YesName(name):
  print "name confirmed"
  if isNeopixelActivated==1:
    i01.setNeopixelAnimation("Color Wipe", 100, 5, 10, 15) 
  if isChatbotActivated==1:
    if isOpenCvActivated==1:
      i01.cameraOn()
      i01.startedGesture()
      fr=i01.vision.setActiveFilter("FaceRecognizer")
      # set the name on the filter that will be used for the saved examples
      fr.trainName = name
      # set the filter to be in training mode (Where it learns new images)
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      i01.setHeadVelocity(70, 70, 70)
      i01.moveHead(90,90,20)
      sleep(1.3)
      i01.moveHead(90,90,170)
      sleep(2)
      i01.moveHead(90,90,90)
      # now that we have new examples, let's re-train the face recognizer with all our examples.
      fr.train()
      # after we've retrained the model.. start recognizing again
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      i01.finishedGesture()
      i01.opencv.disableFilter("FaceRecognizer")
      i01.chatBot.getResponse("SYSTEM_SAY_HELLO")
    else:
      errorSpokenFunc('OpenCvNoWorky')
