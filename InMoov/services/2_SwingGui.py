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
  shutdown()
