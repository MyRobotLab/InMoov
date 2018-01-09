# ##############################################################################
#                 TIMERS ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################
HealthCheck = Runtime.start("HealthCheck","Clock")
HealthCheck.setInterval(60000)

batterieLevel=100
errorBat=1
try:
  if Runtime.getBatteryLevel():
    batterieLevel = Runtime.getBatteryLevel()
    print "battery :",batterieLevel
    errorBat=0
except:
  pass


def HealthCheck_def(timedata):
  global batterieLevel

  if not errorBat:
    if Runtime.getBatteryLevel():batterieLevel = Runtime.getBatteryLevel()
  i01.setBatteryLevel(int(batterieLevel))
  print "battery :",batterieLevel
  
  if RobotIsErrorMode==1:
    if error_red:
      i01.setNeopixelAnimation("Flash Random", 255, 0, 0, 5)
      
  else:HealthCheck.stopClock()
  

HealthCheck.addListener("pulse", python.name, "HealthCheck_def")    
HealthCheck.startClock()

