sensorTimer = Runtime.createAndStart("sensorTimer","Clock")
sensorTimer.addListener("pulse", python.name, "sensorTimerRoutine")
sensorTimer.addListener("clockStarted", python.name, "sensorTimerStart")  
sensorTimer.addListener("clockStopped", python.name, "sensorTimerStop")

#loop every 1000ms
sensorTimer.setInterval(1000)

def sensorTimerStart():rightHandSensorON()

def sensorTimerStop():rightHandSensorOFF()

def sensorTimerRoutine(timedata):
  if rightThumbSensorPin == "No thumb right pressure":
    print "No thumb right pressure"
    i01.rightHand.thumb.moveTo(180)
  else:i01.rightHand.thumb.disable()
  
  if rightIndexSensorPin == "No index right pressure":
    print "No index right pressure"
    i01.rightHand.index.moveTo(125)
  else:i01.rightHand.index.disable()
  
  #TODO fingers like upside
