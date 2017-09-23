def stopTracking():
  if (i01.RobotIsTrackingSomething()):
    if i01.headTracking:i01.headTracking.stopTracking()
    if i01.eyesTracking:i01.eyesTracking.stopTracking()
  if isHeadActivated:
    i01.head.setOverrideAutoDisable(False)
    i01.setHeadVelocity(25,25,25)
    head.rest()