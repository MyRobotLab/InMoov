def memorizePerson():
  i01.chatBot.getResponse("SAY " + "What name should I memorize for this person")
  #this sends back to the inmoovGestures.AIML

def YesName():
  print "name confirmed"
  if isNeopixelActivated==1:
    i01.setNeopixelAnimation("Color Wipe", 100, 5, 10, 15) 
  if isChatbotActivated:
    i01.cameraOn()
    fr=i01.vision.setActiveFilter("FaceRecognizer")
    #TODO set name of the person to be trained via the AIML
    fr.train()
    sleep(2)
    i01.opencv.disableFilter("FaceRecognizer")
