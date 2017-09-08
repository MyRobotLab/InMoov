def stopTracking():
  if (i01.RobotIsOpenCvCapturing()):
    if i01.headTracking:i01.headTracking.stopTracking()
    if i01.eyesTracking:i01.eyesTracking.stopTracking()
  i01.finishedGesture()

