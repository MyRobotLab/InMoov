def stopTracking():
  if (i01.RobotIsTrackingSomething()):
    if i01.headTracking:i01.stopHeadTracking()
    if i01.eyesTracking:i01.eyesTracking.stopTracking()
    # restore "autoDisable" original user status
    i01.head.rollNeck.setOverrideAutoDisable(False)
    stopfacerecognizer()