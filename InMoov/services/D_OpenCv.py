# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  

##Please use InMoov Vision GUI tab for i01.opencv configuration ( camera / grabber etc ... )
##You can also set custom parameters from script as usual :
#i01.vision.setOpenCVenabled(True)
#i01.vision.addPreFilter("Flip")
#i01.opencv.setCameraIndex(1)
#i01.opencv.setGrabberType("Sarxos")


# ##############################################################################
#                 SERVICE START
# ##############################################################################
i01.vision.setOpenCVenabled(True)
if i01.vision.openCVenabled:
  i01.vision.setOpenCVenabled(i01.startOpenCV())
  if not i01.vision.openCVenabled:
    errorSpokenFunc('OpenCvNoWorky','camera '+i01.opencv.getCameraIndex())
  else:
    python.subscribe("i01.opencv", "publishRecognizedFace")
    python.subscribe("i01.opencv", "publishClassification")
  

def onRecognizedFace(name):
  print name
  # robot reaction if recognized face ( todo beter reaction... )
  if isChatbotActivated:
    chatBot.setUsername(unicode(name,'utf-8'))
    chatBot.getResponse("SYSTEM_SAY_HELLO")