def fullspeed():
  inMoov.setNeopixelAnimation("Color Wipe", 200, 0, 0, 1)
  sleep(1)
  inMoov.setNeopixelAnimation("Ironman", 0, 0, 255, 1)
  if isRightHandActivated:
    inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
      
  if isLeftHandActivated:
    inMoov.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
      
  if isRightArmActivated:
    inMoov.setArmVelocity("right", -1, -1, -1, -1)
    
  if isLeftArmActivated:
    inMoov.setArmVelocity("left", -1, -1, -1, -1)
  
  if isHeadActivated:
    inMoov.setHeadVelocity(-1, -1, -1)
  
  if isTorsoActivated:
    inMoov.setTorsoVelocity(-1, -1, -1)
      
  if isEyeLidsActivated:
    inMoov.setEyelidsVelocity(-1,-1)

