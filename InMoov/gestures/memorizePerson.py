from org.myrobotlab.opencv import OpenCVFilterFaceRecognizer
def memorizePerson():
  i01.chatBot.getResponse("SAY " + "What name should I memorize for this person")

def YesName(name):
  print "name confirmed"
  if isNeopixelActivated==1:
    i01.setNeopixelAnimation("Color Wipe", 100, 5, 10, 15) 
  if isChatbotActivated:
    i01.cameraOn()
    fr=i01.vision.setActiveFilter("FaceRecognizer")
    # set the name on the filter that will be used for the saved examples
    fr.trainName = name
    # set the filter to be in training mode (Where it learns new images)
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
    # wait 5 seconds for the example images to be taken.
    sleep(2)
    # now that we have new examples, let's re-train the face recognizer with all our examples.
    fr.train()
    # after we've retrained the model.. start recognizing again
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
    i01.opencv.disableFilter("FaceRecognizer")
    i01.chatBot.getResponse("WAKE_UP")
