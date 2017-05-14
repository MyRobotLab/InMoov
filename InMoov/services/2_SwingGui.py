# ##############################################################################
#                 SWINGGUI SERVICE
# ##############################################################################
# 

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if LaunchSwingGui:
  SwingGui=Runtime.createAndStart("SwingGui", "SwingGui")
  SwingGui.closeTimeout=10
python.subscribe(runtime.getName(),"publishShutdown")

def onShutdown(data):
  talk(lang_shutDown)
  StopNeopixelAnimation()
  i01.halfSpeed()
  i01.rest()
  sleep(7)
  i01.disable()
  #cli.stopService()
