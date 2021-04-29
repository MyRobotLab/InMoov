## A small gesture to test a pinch of the right hand using finger sensors
def testSensor():
  rest()
  i01.startedGesture()
  i01.setHandSpeed("left", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setHandSpeed("right", 22.0, 22.0, 22.0, 22.0, 22.0, 100.0)
  i01.setArmSpeed("right", 59, 59, 59, 43.0)
  i01.setArmSpeed("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadSpeed(100.0, 100.0)
  i01.setTorsoSpeed(22.0, 13.0, 100.0)
  i01.moveHead(90.0,90.0,95.0,90.0,0.0,90.0)
  i01.moveArm("left",5.0,90.0,30.0,12.0)
  i01.moveHand("left",0.0,0.0,0.0,0.0,57.0)
  i01.rightArm.moveToBlocking(40.0,90.0,49.0,12.0)
  i01.moveTorso(90.0,90.0,90.0)
  ## TODO fix the bug if we don't finish the gesture at this point
  ## the pressure sensors don't work
  i01.finishedGesture()
  if rightHandSensorActivated:
    rightHandSensorON() # this enable the pins sensors
    sleep(1.5)
    rightThumbPressure=1 # Pressure range between 0-3
    rightIndexPressure=1 # It defines how much pressure we want for this gesture
    rightMajeurePressure=1
    i01.rightHand.thumb.moveTo(180)
    i01.rightHand.index.moveTo(180)
    i01.rightHand.majeure.moveTo(180)
    sleep(2) # the time to give pins sensors to feel something
    rightHandSensorOFF() # this disable the pins sensors
  else:
    i01.moveHand("right",140,160,20,3,0,11)
