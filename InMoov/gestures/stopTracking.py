def stopTracking():
  if (i01.vision.isTracking()):
    i01.stopTracking()
    i01.head.rollNeck.setOverrideAutoDisable(False)