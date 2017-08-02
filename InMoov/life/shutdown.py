# ##############################################################################
#                 ROBOT SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'shutdown' 'extinction' 'afsluiten'
###############################################################################


def shutdown():
  if isChatbotActivated:RemoveFile(mrlWasNotCleanlyShutdownedFile)
  switchOnAllNervo()
  StopNeopixelAnimation()
  if isOpenCvActivated:opencv.stopCapture()
  if isKinectActivated:openni.stopCapture()