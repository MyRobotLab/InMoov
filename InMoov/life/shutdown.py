# ##############################################################################
#                 ROBOT SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'shutdown' 'extinction' 'afsluiten'
###############################################################################


def shutdown():
  talk(lang_shutDown)
  StopNeopixelAnimation()
  i01.halfSpeed()
  i01.rest()
  sleep(7)
  if isOpenCvActivated:opencv.stopCapture()
  i01.disable()
  switchOffAllNervo()
  killRuntime()