def stopTracking():
  if (inMoov.RobotIsTrackingSomething()):
    if inMoov.headTracking:inMoov.stopHeadTracking()
    if inMoov.eyesTracking:inMoov.eyesTracking.stopTracking()
    # restore "autoDisable" original user status
    inMoov.head.rollNeck.setOverrideAutoDisable(False)
    stopfacerecognizer()