# ##############################################################################
#                 ROBOT SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'shutdown' 'extinction' 'afsluiten'
###############################################################################


def shutdown():
  switchOnAllNervo()
  talk(lang_shutDown)
  StopNeopixelAnimation()
  i01.halfSpeed()
  i01.rest()
  if isEyeLidsActivated:
    eyelids.autoBlink(False)
    eyelids.eyelidleft.moveTo(180)
    eyelids.eyelidright.moveTo(180)
  sleep(7)
  if isOpenCvActivated:opencv.stopCapture()
  i01.disable()
  switchOffAllNervo()
  killRuntime()